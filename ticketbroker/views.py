from django.shortcuts import render, redirect, get_object_or_404

from .models import Ticket
from .forms import TicketCreationForm


def home(request):
    if request.user.is_authenticated:
        tickets_by_user = Ticket.objects.filter(requested_by=request.user)
        return render(request, 'ticketbroker/user_home.html', {
            'tickets_by_user': tickets_by_user
        })
    return render(request, 'core/not_authenticate.html', {})


def create_ticket(request):
    if request.method == "POST":
        form = TicketCreationForm(request.POST)

        if form.is_valid():
            new_ticket = Ticket(
                reason=form.cleaned_data["reason"],
                where=form.cleaned_data["where"],
                when=form.cleaned_data["when"],
                duration=form.cleaned_data["duration"],
                requested_by=request.user
            )

            new_ticket.save()

            return redirect("user_home")
    else:
        form = TicketCreationForm()

    return render(request, "ticketbroker/create_ticket.html", {'form': form})
