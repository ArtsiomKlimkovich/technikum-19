// Composite_UML (Fasada 5)
class Component {
    void operation() { }
}

class Leaf : Component{
    public void operation() { }
}

class Composite : Component {
    List<Composite> composites = new List<Composite>();

    public void add(Composite composite) {
        composites.Add(composite);
    }
    public void operation() { }
    public void add() { }
    public void remove() { }
    public void getChild() { }
}
