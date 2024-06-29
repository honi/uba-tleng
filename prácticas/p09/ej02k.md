# Ejercicio 2k

```
G11 = ⟨{S,T}, {a,b}, P11, S⟩

P11:
S → b | Sb | Tb
T → aTb | ab
```

Observando las producciones vemos que:
- `S` genera una cantidad arbitraria de `b` a la derecha de la cadena, generando siempre al menos una `b`.
- `T` genera cadenas con `a` y `b` balanceados, de la forma $a^nb^n$.
- Si desde `S` producimos `T`, ya no podemos volver a `S`.

La gramática entonces produce 1 o más `b` a derecha, y luego (opcionalmente) puede producir a izquierda una cadena $a^nb^n$.

Luego resulta que el lenguaje generado es: $\{ a^n b^m \mid m > n \}$.

**Eliminación de la recursión a izquierda de `S`**

```
G11 = ⟨{S,R,T}, {a,b}, P11, S⟩

P11:
S → bR | TbR
R → bR | λ
T → aTb | ab
```

**Factorización a izquierda de `a` en `T`**

```
G11 = ⟨{S,R,T,P}, {a,b}, P11, S⟩

P11:
S → bR | TbR
R → bR | λ
T → aP
P → Tb | b
```

**Anulables**

```
R ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(bR) ∪ Prim(TbR) = {a, b}
Prim(R) = Prim(bR) = {b}
Prim(T) = Prim(aP) = {a}
Prim(P) = Prim(Tb) ∪ Prim(b) = {a, b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(R) = Sig(S) ∪ Sig(R) = {$}
Sig(T) = Prim(b) = {b}
Sig(P) = {}
```

**Símbolos directrices**

```
SD(S → bR) = Prim(bR) = {b}
SD(S → TbR) = Prim(TbR) = {a}
SD(R → bR) = Prim(bR) = {b}
SD(R → λ) = Sig(R) = {$}
SD(T → aP) = Prim(aP) = {a}
SD(P → Tb) = Prim(Tb) = {a}
SD(P → b) = Prim(b) = {b}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|`S`|`S → TbR`|`S → bR`||
|`R`||`R → bR`|`R → λ`|
|`T`|`T → aP`|||
|`P`|`P → Tb`|`P → b`||

</div>
