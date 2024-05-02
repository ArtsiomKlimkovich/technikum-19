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
