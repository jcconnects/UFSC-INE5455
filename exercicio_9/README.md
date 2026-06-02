# Exercício 9 — Selenium

## exercicio1.side

Teste gravado para a extensão **Selenium IDE**. Abre `google.com`, digita o nome no campo de busca e clica em pesquisar.

### Como executar

1. Instale a extensão **Selenium IDE** no navegador:
   - Chrome: https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd
   - Firefox: https://addons.mozilla.org/firefox/addon/selenium-ide/
2. Abra a extensão (ícone na barra do navegador).
3. Escolha **Open an existing project** e selecione o arquivo `exercicio1.side`.
4. Na aba **Tests**, selecione `Test1`.
5. Clique no botão **Run current test** (▶) no topo da janela do Selenium IDE.
6. O navegador será aberto automaticamente e executará as ações gravadas.

## exercicio2.py

Testes Selenium WebDriver em Python para a calculadora do DuckDuckGo. Cobre 4 cenários:

- **A** — Soma de dois números.
- **B** — Multiplicação seguida de divisão por 10.
- **C** — Duas operações (uma subtração), verifica resultado final.
- **D** — Três operações distintas, valida cada resultado e a presença no histórico.

### Pré-requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) instalado
- Google Chrome instalado (Selenium gerencia o ChromeDriver automaticamente)

### Como executar

```bash
uv sync
uv run pytest exercicio2.py -v
```
