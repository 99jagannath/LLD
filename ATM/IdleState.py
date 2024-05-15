from State import State
from HasCardState import HasCardState

class IdleState(State):

    def insertCard(self, atm):
        print("Card has been inserted")
        return atm.setATMState(HasCardState())