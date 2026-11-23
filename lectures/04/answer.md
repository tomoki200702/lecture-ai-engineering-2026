# 第4回 解答

## 演習

- 基準別の一致率（直す前）：根拠　/　、範囲　/　、ヒント　/　、分かりやすさ　/　、回の表示　/　
- 要確認の件数（直す前）：
- 直した基準と、書き足した方針：
- 基準別の一致率と要確認の件数（直した後）：
- 講師のラベルと自分のラベルで判定が違った項目と、そう判定した理由：
- 気づき・疑問：

## 宿題

取り組んだレベルは発展。

### やったこと

SWE-bench Verifiedから、数式処理ライブラリSymPyの問題を3件読んだ。 [公開データセット](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified)

1. 単位行列の和（`sympy__sympy-12419`）。対角の `1` を数えれば和は `n` と分かる。誤って `0` になる原因を探すには、添字が記号のときの計算を追う必要がある。 [元のIssue](https://github.com/sympy/sympy/issues/12300)
2. 列の挿入（`sympy__sympy-13647`）。途中に2列を挿入すると、右側の成分が別の行にずれる。修正するには、挿入前後の列番号の対応を調べる必要がある。 [元のIssue](https://github.com/sympy/sympy/issues/13643)
3. `Max` の変換（`sympy__sympy-15345`）。Mathematica用の出力で必要な角括弧が丸括弧になる。関数を文字列に変換する処理を探すところから直せそうだ。 [元のIssue](https://github.com/sympy/sympy/issues/15344)

### 結果

元のSWE-benchは、12のPythonリポジトリの不具合報告と修正PRを集めている。VerifiedではPythonの開発経験がある93人が候補1,699件を分担し、1件につき3人が、問題文の明確さと正しい修正をテストで合格にできるかを確認した。約1,160件（68.3％）を除外し、残りから500件を選んだ。 [SWE-benchの論文](https://arxiv.org/abs/2310.06770) ・ [OpenAIの公開資料](https://openai.com/index/introducing-swe-bench-verified/)

Verifiedでは、モデルの修正で不具合が直り、既存の動作が保たれるかをテストで採点する。第4回の演習では、講師1人が用意した10件の回答を人とLLMが判定し、一致率を確かめる。回の表示はコードで確認する。 [SWE-bench Verifiedの採点方法](https://openai.com/index/introducing-swe-bench-verified/) ・ [第4回の演習](https://github.com/matsuolab/lecture-ai-engineering-2026/blob/main/lectures/04/problem.md)

### 気づき・疑問

テストの作り方次第で、動作を正しく直した修正でも不合格になりうる点が気になった。文章を評価するときにも、採点基準を具体的にした結果、正しい言い換えまで落としていないかを確かめたい。

Codexをサポート役として使った。
