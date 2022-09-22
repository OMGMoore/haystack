import pytest

from haystack.document_stores import BaseDocumentStore
from haystack.nodes.retriever import MultihopEmbeddingRetriever

from test.nodes.retrievers.dense import ABC_TestDenseRetrievers


class TestMultiHopRetriever(ABC_TestDenseRetrievers):
    @pytest.fixture()
    def retriever(self, docstore: BaseDocumentStore):
        retriever = MultihopEmbeddingRetriever(
            document_store=docstore,
            embedding_model="deutschmann/mdr_roberta_q_encoder",  # or "facebook/dpr-ctx_encoder-single-nq-base"
            use_gpu=False,
        )
        docstore.update_embeddings(retriever=retriever)