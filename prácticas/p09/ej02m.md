# Ejercicio 2m

## Primer intento

```
G13 = ⟨{S,A}, {a,c}, P13, S⟩

P13:
S → Sc | cA | λ
A → aA | a
```

**Eliminación de la recursión a izquierda de `S`**

```
G13 = ⟨{S,A,T}, {a,c}, P13, S⟩

P13:
S → cAT | T
T → cT | λ
A → aA | a
```

**Factorización a izquierda de `A`**

```
G13 = ⟨{S,T,A,P}, {a,c}, P13, S⟩

P13:
S → cAT | T
T → cT | λ
A → aP
P → A | λ
```

**Anulables**

```
S ⇒* λ
T ⇒* λ
P ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(cAT) ∪ Prim(T) = {c}
Prim(T) = Prim(cT) = {c}
Prim(A) = Prim(aP) = {a}
Prim(P) = Prim(A) = {a}
```

**Siguientes**

```
Sig(S) = {$}
Sig(T) = Sig(S) ∪ Sig(T) = {$}
Sig(A) = Prim(T) ∪ Sig(S) ∪ Sig(P) = {c, $}
Sig(P) = Sig(A) = {c, $}
```

**Símbolos directrices**

```
SD(S → cAT) = Prim(cAT) = {c}
SD(S → T) = Prim(T) ∪ Sig(S) = {c, $}
SD(T → cT) = Prim(cT) = {c}
SD(T → λ) = Sig(T) = {$}
SD(A → aP) = Prim(aP) = {a}
SD(P → a) = Prim(a) = {a}
SD(P → λ) = Sig(P) = {c, $}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular: `SD(S → cAT) ∩ SD(S → T) = {c} ≠ Ø`.

## Segundo intento

El lenguaje generado es `ca+c*|c*`. El conflicto proviene de la primera `c`, no podemos saber si después van a venir las `a` o si estamos en el segundo caso donde es una cadena de todas `c`.

Agregamos un nuevo start symbol para generar la primer `c` sin conflictos. El lenguaje generado es el mismo pero lo podemos pensar de esta otra forma: `c(a+c*|c+)|λ`.

```
G13 = ⟨{S,T,A,P,Q}, {a,c}, P13, Q⟩

P13:
Q → cS | λ
S → AT | T
T → cT | λ
A → aP
P → A | λ
```

**Anulables**

```
Q ⇒* λ
S ⇒* λ
T ⇒* λ
P ⇒* λ
```

**Primeros**

```
Prim(Q) = Prim(cS) = {c}
Prim(S) = Prim(AT) ∪ Prim(T) = {a, c}
Prim(T) = Prim(cT) = {c}
Prim(A) = Prim(aP) = {a}
Prim(P) = Prim(A) = {a}
```

**Siguientes**

```
Sig(Q) = {$}
Sig(S) = Sig(Q) = {$}
Sig(T) = Sig(S) ∪ Sig(T) = {$}
Sig(A) = Prim(T) ∪ Sig(S) ∪ Sig(P) = {c, $}
Sig(P) = Sig(A) = {c, $}
```

**Símbolos directrices**

```
SD(Q → cS) = Prim(cS) = {c}
SD(Q → λ) = Sig(Q) = {$}
SD(S → AT) = Prim(AT) = {a}
SD(S → T) = Prim(T) ∪ Sig(S) = {c, $}
SD(T → cT) = Prim(cT) = {c}
SD(T → λ) = Sig(T) = {$}
SD(A → aP) = Prim(aP) = {a}
SD(P → a) = Prim(a) = {a}
SD(P → λ) = Sig(P) = {c, $}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`c`|`$`|
|-|-|-|-|
|`Q`||`Q → cS`|`Q → λ`|
|`S`|`S → AT`|`S → T`|`S → T`|
|`T`||`T → cT`|`T → λ`|
|`A`|`A → aP`|||
|`P`|`P → a`|`P → λ`|`P → λ`|

</div>
