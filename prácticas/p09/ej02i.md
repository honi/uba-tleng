# Ejercicio 2i

```
G9 = ⟨{S,A,L}, {(,),,,f,x}, P9, S⟩

P9:
S → fA
A → (L)
L → x | x,L | S
```

Es una gramática que produce "llamados a funciones" con ciertas características:
- Todas las funciones tienen al menos un argumento.
- Admite una cantidad arbitraria de niveles de composición.
- Solo se puede componer funciones en el último argumento.

Por ejemplo estas cadenas están en el lenguaje:
- `f(x)`
- `f(x,x)`
- `f(f(x))`
- `f(x,f(x))`
- `f(x,x,f(f(x,f(x,x,x,x,f(x)))))`

La gramática es ambigua en las producciones de `L` (la lista de argumentos). Al consumir el símbolo `x` no sabemos si es el último argumento o si hay más. Modifiquemos las producciones de `L` para consumir `x` en una única producción y luego ver si hay más argumentos o no desde un nuevo no terminal `T` (factorización a izquierda).

```
G9 = ⟨{S,A,L,T}, {(,),,,f,x}, P9, S⟩

P9:
S → fA
A → (L)
L → xT | S
T → ,L | λ
```

**Anulables**

```
T ⇒* λ
```

**Primeros**

```
Prim(S) = {f}
Prim(A) = {(}
Prim(L) = Prim(xT) ∪ Prim(S) = {x, f}
Prim(T) = {,}
```

**Siguientes**

```
Sig(S) = Sig(L) ∪ {$} = {), $}
Sig(A) = Sig(S) = {), $}
Sig(L) = Prim()) ∪ Sig(T) = {)}
Sig(T) = Sig(L) = {)}
```

**Símbolos directrices**

```
SD(S → fA) = Prim(fA) = {f}
SD(A → (L)) = Prim((L)) = {(}
SD(L → xT) = Prim(xT) = {x}
SD(L → S) = Prim(S) = {f}
SD(T → ,L) = Prim(,L) = {,}
SD(T → λ) = Sig(T) = {)}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`f`|`(`|`)`|`x`|`,`|`$`|
|-|-|-|-|-|-|-|
|`S`|`S → fA`|||||
|`A`||`A → (L)`||||
|`L`|`L → S`|||`L → xT`||
|`T`|||`T → λ`||`T → ,L`|

</div>

**Seguimiento**

| Pila | Entrada | Producción |
|-|-|-|
|`S$`|`f(x,f(x))$`|`S → fA`|
|~~`f`~~ `A$`|~~`f`~~ `(x,f(x))$`|`A → (L)`|
|~~`(`~~ `L)$`|~~`(`~~ `x,f(x))$`|`L → xT`|
|~~`x`~~ `T)$`|~~`x`~~ `,f(x))$`|`T → ,L`|
|~~`,`~~ `L)$`|~~`,`~~ `f(x))$`|`L → S`|
|`S)$`|`f(x))$`|`S → fA`|
|~~`f`~~ `A)$`|~~`f`~~ `(x))$`|`A → (L)`|
|~~`(`~~ `L))$`|~~`(`~~ `x))$`|`L → xT`|
|~~`x`~~ `T))$`|~~`x`~~ `))$`|`T → λ`|
|~~`))$`~~|~~`))$`~~|**Aceptada**|
