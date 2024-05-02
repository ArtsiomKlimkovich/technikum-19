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
