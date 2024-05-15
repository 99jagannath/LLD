from State import State
from IdleState import IdleState
from SelectOperationState import SelectOperationState

class HasCardState(State):

    def authenticatePin(self, atm, card, pin):
        if card.validatePin(pin):
            atm.setATMState(SelectOperationState())

        else:
            print("Invalid Pin")
            self.exit()

    def returnCard(self):
        print("returning card")

    def exit(self, atm):
        self.returnCard()
        atm.setATMState(IdleState())