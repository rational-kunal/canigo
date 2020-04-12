from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from ticketbroker.models import Ticket


@staff_member_required
def home(request):
    all_tickets = Ticket.objects.filter()
    return render(request, 'reviewer/staff_home.html', {
        'heading': 'All Tickets',
        'all_ticket': all_tickets
    })


@staff_member_required
def approve_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.approved = True
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
def approved_ticket_list(request):
    all_approved_tickets = Ticket.objects.filter(approved=True)
    return render(request, 'reviewer/staff_home.html', {
        'heading': 'Approved Tickets',
        'all_ticket': all_approved_tickets
    })


@staff_member_required
def disapprove_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.approved = False
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
def disapproved_ticket_list(request):
    all_disapproved_tickets = Ticket.objects.filter(approved=False)
    return render(request, 'reviewer/staff_home.html', {
        'heading': 'Disapproved Tickets',
        'all_ticket': all_disapproved_tickets
    })