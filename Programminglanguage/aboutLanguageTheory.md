
## 1. 用語

<!-- 

```dot
graph G {
    node [
        shape = box
    ]
    subgraph cluster0 {
        label="言語";
        color=black;
        
        subgraph cluster0 {
            label="文字列";
            b [label="文字"];
        }
        
    }
}
``` -->



#### 文字列
集合$\Sigma$中の全ての文字を任意の回数使用して作られる0文字以上の列

例：$\Sigma=\{a,b\}$のとき<br>
- ""
- "b"
- "aababaa"
- "aaaaaaaaaaaaabbbaaaaabbabbababbabbabaaaaa"

など


|文字列の特殊例|表現方法|
|:----:|:----:|
|文字列$w$の長さ| &#124;$w$&#124; |
|$N$回連続する文字$a$| $a^N$|
|&#124;$w$&#124;$=0$ <br>(長さが0の文字列$w$)|$\varepsilon$|
|２つの文字列$x,y$の連結|$xy (\neq yx)$|
|$\Sigma$からなる<br>全ての文字列の集合|$\Sigma^*$|
|$\Sigma$からなる<br>空白文字を除く<br>全ての文字列の集合|$\Sigma^+$|



#### 言語$L$

文字列の集合であり、言語$L$は必ず$\Sigma^*$の部分集合となる。


#### オートマトン

ある文字列がある言語$L$に含まれるか否かを判定するための機械

```dot
digraph {
    graph [
        label="文字列が言語Lに",
        labelloc="t"
    ]

    edge []

    A [label="文字列"];
    B [label="受理(accept)"];
    C [label="却下(reject)"];

     A -> B [label="含まれる",labeljust = "c"];
     A -> C [label="含まれない"];

}

```

有限オートマトン



決定性有限オートマトン(DFA)

非決定性有限オートマトン
(NFA)











## 2. 