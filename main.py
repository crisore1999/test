from model.Distributore import Distributore

distributore = Distributore("Bibita")
distributore.aggiungiBevanda("A", "Acqua", 0.20)
distributore.aggiungiBevanda("B", "Cocacola", 0.30)
distributore.aggiungiBevanda("C", "Birra", 1.00)

distributore.getPrice("A")

distributore.caricaTessera("12", 5.5)
distributore.caricaTessera("21", 10.0)
distributore.caricaTessera("99", 0.75)

distributore.aggiornaColonna("Acqua minerale", 40)
distributore.aggiornaColonna("Cocacola", 1)
distributore.aggiornaColonna("Birra", 50)
distributore.aggiornaColonna("Acqua frizzante", 50)

distributore.erogaBibita("A", 12)

