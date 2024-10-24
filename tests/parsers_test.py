""" Parsers unit tests
"""

import os
import sys
import inspect
import textwrap

import pytest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from dou_dag_generator import DouDigestDagGenerator, YAMLParser, DAGConfig


@pytest.mark.parametrize(
    "filepath, result_tuple",
    [
        (
            "basic_example.yaml",
            {
                "id": "basic_example",
                "description": "DAG de teste",
                "search": [
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": None,
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "search_date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "schedule": None,
                    "dataset": None,
                    "description": "DAG de teste",
                    "skip_null": True,
                    "doc_md": None,
                    "tags": {"dou", "generated_dag"},
                    "owner": [],
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados "
                    "foi encontrado nesta consulta",
                },
            },
        ),
        (
            "all_parameters_example.yaml",
            {
                "id": "all_parameters_example",
                "schedule": "0 8 * * MON-FRI",
                "dataset": None,
                "description": "DAG exemplo utilizando todos os demais parâmetros.",
                "doc_md": None,
                "tags": {"dou", "generated_dag", "projeto_a", "departamento_x"},
                "owner": ["pessoa 1", "pessoa 2"],
                "search": [
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": "Pesquisa no DOU",
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["SECAO_1", "EDICAO_SUPLEMENTAR"],
                        "date": "MES",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": True,
                        "force_rematch": True,
                        "full_text": True,
                        "use_summary": True,
                        "department": None,
                    }
                ],
                "report": {
                    "skip_null": True,
                    "emails": ["dest1@economia.gov.br", "dest2@economia.gov.br"],
                    "subject": "Assunto do Email",
                    "attach_csv": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi "
                    "encontrado nesta consulta",
                },
            },
        ),
        (
            "terms_from_db_example.yaml",
            {
                "id": "terms_from_db_example",
                "description": "DAG de teste",
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "schedule": None,
                "dataset": None,
                "search": [
                    {
                        "terms": {
                            "from_airflow_variable": None,
                            "from_db_select": {
                                "sql": (
                                    "SELECT 'cloroquina' as TERMO, 'Ações inefetivas' as GRUPO "
                                    "UNION SELECT 'ivermectina' as TERMO, 'Ações inefetivas' as GRUPO "
                                    "UNION SELECT 'vacina contra covid' as TERMO, 'Ações efetivas' as GRUPO "
                                    "UNION SELECT 'higienização das mãos' as TERMO, 'Ações efetivas' as GRUPO "
                                    "UNION SELECT 'uso de máscara' as TERMO, 'Ações efetivas' as GRUPO "
                                    "UNION SELECT 'distanciamento social' as TERMO, 'Ações efetivas' as GRUPO\n"
                                ),
                                "conn_id": "example_database_conn",
                            }
                        },
                        "header": None,
                        "sources": ["DOU"],
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "MES",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "[String] com caracteres especiais deve estar entre aspas",
                    "attach_csv": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "skip_null": True,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "basic_example_skip_null.yaml",
            {
                "id": "basic_example_skip_null",
                "schedule": None,
                "dataset": None,
                "description": "DAG de teste",
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": ["cimentodaaroeira"],
                        "header": None,
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "skip_null": False,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "markdown_docs_example.yaml",
            {
                "id": "markdown_docs_example",
                "schedule": None,
                "dataset": None,
                "description": "DAG com documentação em markdown",
                "doc_md": textwrap.dedent(
                    """
                    ## Ola!
                    Esta é uma DAG de exemplo com documentação em markdown. Esta descrição é opcional e pode ser definida no parâmetro `doc_md`.

                      * Ah, aqui você também pode usar *markdown* para
                      * escrever listas, por exemplo,
                      * ou colocar [links](graph)!"""
                ).strip(),
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": None,
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "skip_null": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "department_example.yaml",
            {
                "id": "department_example",
                "schedule": None,
                "dataset": None,
                "description": "DAG de teste (filtro por departamento)",
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": ["dados abertos"],
                        "header": None,
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": [
                            "Ministério da Gestão e da Inovação em Serviços Públicos",
                            "Ministério da Defesa",
                        ],
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "skip_null": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "inlabs_example.yaml",
            {
                "id": "inlabs_example",
                "schedule": "0 8 * * MON-FRI",
                "dataset": "inlabs",
                "description": "DAG de teste",
                "doc_md": None,
                "tags": {"dou", "generated_dag", "inlabs"},
                "owner": ["cdata"],
                "search": [
                    {
                        "terms": ["tecnologia", "informação"],
                        "header": None,
                        "sources": ["INLABS"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": True,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": True,
                    "skip_null": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "inlabs_advanced_search_example.yaml",
            {
                "id": "inlabs_advanced_search_example",
                "schedule": None,
                "dataset": "inlabs",
                "description": "DAG de teste",
                "skip_null": True,
                "doc_md": None,
                "tags": {"dou", "generated_dag", "inlabs"},
                "owner": ["cdata"],
                "search": [
                    {
                        "terms": [
                            "designar & ( MGI | MINISTÉRIO FAZENDA)",
                            "instituto & federal ! paraná",
                        ],
                        "header": None,
                        "sources": ["INLABS"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "multiple_searchs_example.yaml",
            {
                "id": "multiple_searchs_example",
                "schedule": "0 8 * * MON-FRI",
                "dataset": None,
                "description": "DAG de teste com múltiplas buscas",
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": "Pesquisa no DOU",
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": True,
                        "force_rematch": True,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    },
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": "Pesquisa no QD",
                        "sources": ["QD"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": True,
                        "force_rematch": True,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    },
                    {
                        "terms": [
                            "dados abertos",
                            "governo aberto",
                            "lei de acesso à informação",
                        ],
                        "header": "Pesquisa no DOU e QD (misto)",
                        "sources": ["DOU", "QD"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": True,
                        "force_rematch": True,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    },
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "skip_null": False,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "hide_filters_example.yaml",
            {
                "id": "hide_filters_example",
                "schedule": "0 8 * * MON-FRI",
                "dataset": None,
                "description": "DAG de teste",
                "doc_md": None,
                "tags": {"dou", "inlabs", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": ["tecnologia", "informação"],
                        "header": "HEADER TEXT",
                        "sources": ["INLABS"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": [
                            "Ministério da Gestão e da Inovação em Serviços Públicos",
                            "Ministério da Defesa",
                        ],
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": True,
                    "skip_null": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": True,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados foi encontrado nesta consulta",
                },
            },
        ),
        (
            "header_and_footer_example.yaml",
            {
                "id": "header_and_footer_example",
                "schedule": "0 8 * * MON-FRI",
                "dataset": None,
                "description": "DAG de teste",
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": ["tecnologia", "informação"],
                        "header": None,
                        "sources": ["DOU"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": None,
                        "dou_sections": ["TODOS"],
                        "date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": False,
                        "force_rematch": False,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "skip_null": True,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "hide_filters": False,
                    "header_text": "<p><strong>Greetings<strong></p>",
                    "footer_text": "<p>Best Regards</p>",
                    "no_results_found_text": "No results found",
                },
            },
        ),
        (
            "qd_list_territory_id_example.yaml",
            {
                "id": "qd_list_territory_id_example",
                "description": "DAG de teste com múltiplos territory_id",
                "schedule": '0 8 * * MON-FRI',
                "dataset": None,
                "doc_md": None,
                "tags": {"dou", "generated_dag"},
                "owner": [],
                "search": [
                    {
                        "terms": [
                            "LGPD",
                            "RIO DE JANEIRO",
                        ],
                        "header": "Teste com múltiplos territory_id",
                        "sources": ["QD"],
                        "sql": None,
                        "conn_id": None,
                        "territory_id": [3300100,3300159,3300209,3305703],
                        "dou_sections": ["TODOS"],
                        "search_date": "DIA",
                        "field": "TUDO",
                        "is_exact_search": True,
                        "ignore_signature_match": True,
                        "force_rematch": True,
                        "full_text": False,
                        "use_summary": False,
                        "department": None,
                    }
                ],
                "report": {
                    "emails": ["destination@economia.gov.br"],
                    "subject": "Teste do Ro-dou",
                    "attach_csv": False,
                    "discord_webhook": None,
                    "slack_webhook": None,
                    "skip_null": False,
                    "hide_filters": False,
                    "header_text": None,
                    "footer_text": None,
                    "no_results_found_text": "Nenhum dos termos pesquisados "
                    "foi encontrado nesta consulta",
                },
            },
        ),
    ],
)
def test_parse(filepath, result_tuple):
    filepath = os.path.join(
        DouDigestDagGenerator().YAMLS_DIR, "examples_and_tests", filepath
    )
    parsed = YAMLParser(filepath=filepath).parse()

    assert parsed.model_dump() == DAGConfig(**result_tuple).model_dump()
