package com.tbc;

public class TicketDispenser {
    private static int currentTurnNumber = 0;

    public static int nextTurnNumber() {
        currentTurnNumber += 1;
        return currentTurnNumber;
    }

    public static Ticket nextTicket() {
        int turnNumber = nextTurnNumber();
        return new Ticket(turnNumber);
    }
}
