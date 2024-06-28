# Ejercicio 2a

```
G1 = ⟨{S,A}, {a,b}, P1, S⟩

P1:
S → aAS | b
A → a | bSA
```

**Anulables**

No hay producciones anulables.

**Primeros**

```
Prim(S) = Prim(a) ∪ Prim(b) = {a, b}
Prim(A) = Prim(a) ∪ Prim(b) = {a, b}
```

**Siguientes**

```
Sig(S) = Prim(A) ∪ {$} = {a, b, $}
Sig(A) = Prim(S) = {a, b}
```

**Símbolos directrices**

```
SD(S → aAS) = Prim(aAS) = Prim(a) = {a}
SD(S → b) = Prim(b) = Prim(b) = {b}
SD(A → a) = Prim(a) = Prim(a) = {a}
SD(A → bSA) = Prim(bSA) = Prim(b) = {b}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|`S`|`S → aAS`|`S → b`||
|`A`|`A → a`|`A → bSA`||

</div>
