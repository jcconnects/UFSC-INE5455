from behave import given, when, then
from mercado_leilao import MercadoLeilao


@when("cadastra o usuario")
def step_impl(context):
    context.mercado = MercadoLeilao()
    try:
        context.mercado.cadastra_usuario(
            context.nome_usuario,
            context.endereco_usuario,
            context.email_usuario,
            context.cpf_usuario,
        )
        context.msg = "Usuario cadastrado com sucesso"
    except Exception as e:
        context.msg = e.__str__()


@then("o sistema retorna a mensagem {mensagem}")
def step_impl(context, mensagem):
    assert mensagem == context.msg
