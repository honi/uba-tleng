# Ejercicio 2d

## Primer intento

```
G4 = ⟨{S,A}, {a,b}, P4, S⟩

P4:
S → aAaa | bAba
A → b | λ
```

**Anulables**

```
A ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(aAaa) ∪ Prim(bAba) = {a, b}
Prim(A) = Prim(b) = {b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(A) = Prim(aa) ∪ Prim(ba) = {a, b}
```

**Símbolos directrices**

```
SD(S → aAaa) = Prim(aAaa) = {a}
SD(S → bAba) = Prim(bAba) = {b}
SD(A → b) = Prim(b) = {b}
SD(A → λ) = Sig(A) = {a, b}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(A → b) ∩ SD(A → λ) = {b} ≠ Ø`.

## Segundo intento

El conflicto proviene desde la producción `S → bAba`. Una vez que usamos esta producción, no sabemos si la siguiente `b` que consumimos es la que le corresponde a la producción `A → b`, o en realidad vamos a usar `A → λ` y la `b` viene por la producción de `S`.

En cualquier caso, notemos que al usar la producción `S → bAba`, después de la primer `b` **siempre** aparece al menos una `b` más. Y con las producciones de `A` podemos elegir colocar la otra `b` o no. Entonces podemos reescribir la producción de `S` y reordenar las `b`, ya que son indistinguibles entre sí (es decir, no importa qué producción colocó cada `b`).

```
G4 = ⟨{S,A}, {a,b}, P4, S⟩

P4:
S → aAaa | bbAa
A → b | λ
```

**Anulables**

```
A ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(aAaa) ∪ Prim(bbAa) = {a, b}
Prim(A) = Prim(b) = {b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(A) = Prim(aa) ∪ Prim(a) = {a}
```

**Símbolos directrices**

```
SD(S → aAaa) = Prim(aAaa) = {a}
SD(S → bbAa) = Prim(bbAa) = {b}
SD(A → b) = Prim(b) = {b}
SD(A → λ) = Sig(A) = {a}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|S|`S → aAaa`|`S → bbAa`||
|A|`A → λ`|`A → b`||

</div>

**Seguimiento**

| Pila | Entrada | Producción |
|-|-|-|
|`S$`|`abaa$`|`S → aAaa`|
|~~`a`~~ `Aaa$`|~~`a`~~ `baa$`|`A → b`|
|~~`baa$`~~|~~`baa$`~~||
