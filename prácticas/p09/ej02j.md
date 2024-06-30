# Ejercicio 2j

## Primer intento

```
G10 = ⟨{S,A}, {a,b}, P10, S⟩

P10:
S → SAa | Aa
A → Aa | b
```

**Anulables**

No hay producciones anulables.

**Primeros**

```
Prim(S) = Prim(S) ∪ Prim(A) = {b}
Prim(A) = Prim(A) ∪ Prim(b) = {b}
```

**Siguientes**

```
Sig(S) = Prim(A) ∪ {$} = {b, $}
Sig(A) = Prim(a) = {a}
```

**Símbolos directrices**

```
SD(S → SAa) = Prim(SAa) = {b}
SD(S → Aa) = Prim(Aa) = {b}
SD(A → Aa) = Prim(Aa) = {b}
SD(A → b) = Prim(b) = {b}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular:
- `SD(S → SAa) ∩ SD(S → Aa) = {b} ≠ Ø`
- `SD(A → Aa) ∩ SD(A → b) = {b} ≠ Ø`

## Segundo intento

La gramática genera el lenguaje `(ba+)+`. Las producciones de `S` hacen recursión a izquierda y generan una lista de `Aa`. Luego, las producciones de `A` también hacen recursión a izquierda y generan una lista de `a`, terminando con una `b` a la cabeza.

Podríamos directamente reescribir la gramática entera, pero intentemos eliminar la recursión a izquierda para ver si con esos cambios evitamos los conflictos. De esta forma tenemos la garantía de que se preserve el lenguaje original.

```
G10 = ⟨{S,A}, {a,b}, P10, S⟩

P10:
S → AaT
T → AaT | λ
A → bR
R → aR | λ
```

**Anulables**

```
T ⇒* λ
R ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(AaT) = {b}
Prim(T) = Prim(AaT) = {b}
Prim(A) = Prim(bR) = {b}
Prim(R) = Prim(aR) = {a}
```

**Siguientes**

```
Sig(S) = {$}
Sig(T) = Sig(S) ∪ Sig(T) = {$}
Sig(A) = Prim(a) = {a}
Sig(R) = Sig(A) ∪ Sig(R) = {a}
```

**Símbolos directrices**

```
SD(S → AaT) = Prim(AaT) = {b}
SD(T → AaT) = Prim(AaT) = {b}
SD(T → λ) = Sig(T) = {$}
SD(A → bR) = Prim(bR) = {b}
SD(R → aR) = Prim(aR) = {a}
SD(R → λ) = Sig(R) = {a}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular: `SD(R → aR) ∩ SD(R → λ) = {a} ≠ Ø`.

## Tercer intento

El problema que tenemos es cuando vemos una `a` desde las producciones de `R`. No sabemos si después vienen más `a`. `R` captura todas las `a` después de una `b` **excepto** la última `a`, que es generada por `S → AaT` y `T → AaT`.

Podemos sacar la `a` de las producciones de `S` y `T` para generarla desde `A` junto a la `b`. Es indistinto cuándo ponemos las `a` ya que son indistinguibles entre sí. De esta forma, `R` genera `a*` y no hay conflictos en los SD, pues después de generar las `a` con las producciones de `R`, o bien termina la cadena, o bien viene una `b`.

```
G10 = ⟨{S,A}, {a,b}, P10, S⟩

P10:
S → AT
T → AT | λ
A → baR
R → aR | λ
```

Ahora se puede ver más claramente que la gramática genera `(ba+)+`, o equivalentemente `(baa*)+`.

**Anulables**

```
T ⇒* λ
R ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(AT) = {b}
Prim(T) = Prim(AT) = {b}
Prim(A) = Prim(baR) = {b}
Prim(R) = Prim(aR) = {a}
```

**Siguientes**

```
Sig(S) = {$}
Sig(T) = Sig(S) ∪ Sig(T) = {$}
Sig(A) = Prim(T) ∪ Sig(S) ∪ Sig(T) = {b, $}
Sig(R) = Sig(A) ∪ Sig(R) = {b, $}
```

**Símbolos directrices**

```
SD(S → AT) = Prim(AT) = {b}
SD(T → AT) = Prim(AT) = {b}
SD(T → λ) = Sig(T) = {$}
SD(A → baR) = Prim(baR) = {b}
SD(R → aR) = Prim(aR) = {a}
SD(R → λ) = Sig(R) = {b, $}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|`S`||`S → AT`||
|`T`||`T → AT`|`T → λ`|
|`A`||`A → baR`||
|`R`|`R → aR`|`R → λ`|`R → λ`|

</div>
