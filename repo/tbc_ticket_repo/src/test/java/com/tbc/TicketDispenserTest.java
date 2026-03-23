package com.tbc;

public class TicketDispenserTest {
    public void testNextTicket() {
        Ticket ticket = TicketDispenser.nextTicket();
        if (ticket.getTurnNumber() <= 0) {
            throw new RuntimeException("turn number should be positive");
        }
    }
}
