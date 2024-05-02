// Fasada 2
class Client {
    WashingMachine washingMachine;
    public void wash(WashingMachine washingMachine) {
        this.washingMachine = washingMachine;
    }
}

class Washing {
    public void wash() { }
}

class Rinsing {
    public void rinse() { }
}

class Spinning {
    public void spin() { }
}
class WashingMachine {

    Washing washing;
    Rinsing rinsing;
    Spinning spinning;

    public void startWashing() { }

    public void washThis() {
        washing = new Washing();
        rinsing = new Rinsing();
        spinning = new Spinning();
    }

    public void method1() { }
}
