# Ejercicio 2b

```
G2 = ⟨{A}, {+,-,a}, P2, A⟩

P2:
A → +AA | -AA | a
```

**Anulables**

No hay producciones anulables.

**Primeros**

```
Prim(A) = Prim(+AA) ∪ Prim(-AA) ∪ Prim(a) = {+, -, a}
```

**Siguientes**

```
Sig(A) = Prim(A) ∪ {$} = {+, -, a, $}
```

**Símbolos directrices**

```
SD(A → +AA) = Prim(+AA) = {+}
SD(A → -AA) = Prim(-AA) = {-}
SD(A → a) = Prim(a) = {a}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`+`|`-`|`a`|
|-|-|-|-|
|A|`A → +AA`|`A → -AA`|`A → a`|

</div>
