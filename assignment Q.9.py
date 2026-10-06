class Product:
    def __init__(self, pid, name, stock, purchase, selling):
        self.pid=pid; self.name=name
        self.stock=stock; self.purchase=purchase; self.selling=selling

class Inventory:
    def __init__(self):
        self.items={}

    def add(self, product):
        self.items[product.pid]=product

    def __add__(self, other):
        merged=Inventory()
        for inv in [self,other]:
            for pid,p in inv.items.items():
                if pid not in merged.items:
                    merged.items[pid]=Product(pid,p.name,p.stock,p.purchase,p.selling)
                else:
                    mp=merged.items[pid]
                    mp.stock+=p.stock
                    mp.purchase=min(mp.purchase,p.purchase)
                    mp.selling=max(mp.selling,p.selling)
        return merged

    def summary(self):
        for p in self.items.values():
            print(f"{p.pid} {p.name} stock={p.stock} purchase={p.purchase} selling={p.selling}")

# ---------------- SAMPLE INPUT ----------------
invA=Inventory()
invA.add(Product("P1","Pen",10,5,8))
invB=Inventory()
invB.add(Product("P1","Pen",7,4,9))
invB.add(Product("P2","Notebook",20,15,25))

merged=invA+invB
merged.summary()
