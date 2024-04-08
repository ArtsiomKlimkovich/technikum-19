// Fasada 1
class USer {}

class Activity {
    private string type;
    public string time;
}

class Address {
    public string street;
    public string code;
    public string city;
}

class Worker : USer {
    private string position;
    protected string salary;
    Activity activity;
    Address address;

    public void setActivity(Activity activity) { // kiedy agregacja to robimy set
        this.activity = activity;
    }
    public void addAddress (Address address) { // kiedy asocjacja robimy inna nazwe niz set
        this.address = address;
    }

    public void setParameters() {
        Address a = new Address();
        a.city = "Poznan";
        this.address = a;
    }
}

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

// Fasada 3
interface Car {
    public void build();
}

class Chevrolet : Car {
    public void build() {}
}

class BMW : Car {
    public void build() { }
}

class Renault : Car {
    public void build() { }
}

class FasadeForCar {
    Car Chevrolet;
    Car BMW;
    Car Renault;

    public FasadeForCar() {}

    public void buildChevrolet() { }
    public void buildBMW() { }
    public void buildRenault() { }
}
