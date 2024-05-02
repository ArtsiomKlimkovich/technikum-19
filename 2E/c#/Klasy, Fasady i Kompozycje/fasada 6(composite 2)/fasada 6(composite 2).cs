// Composite 2(Fazada 6)
abstract class Graphic {
    public abstract void draw();
}

class Line : Graphic {
    public override void draw() { }
}

class Rectangle : Graphic {
    public override void draw() { }
}

class Text : Graphic {
    public override void draw() { }
}

class Picture : Graphic {
    List<Graphic> list = new List<Graphic>();
    public override void draw() { }
    public void add(Graphic g) {
        list.Add(g);
    }

    public void remove(Graphic g) { }

    public void getChild(int i) { }

}
