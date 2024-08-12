import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer

class DocumentDataset(Dataset):
    def __init__(self, documents, labels, vocab, tokenizer, max_length=120):
        self.documents = documents
        self.labels = torch.tensor(labels).float()
        self.max_length = max_length
        self.vocab = vocab
        self.tokenizer = tokenizer

    def preprocess(self, text):
        tokens = self.tokenizer(text)
        tokens = tokens[:self.max_length]
        if len(tokens) < self.max_length:
            tokens += ['<pad>'] * (self.max_length - len(tokens))
        return torch.tensor([self.vocab[token] for token in tokens])

    def __len__(self):
        return len(self.documents)

    def __getitem__(self, idx):
        text = self.preprocess(self.documents[idx])
        label = self.labels[idx]
        return text, label

class DocumentClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(DocumentClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc = nn.Linear(embedding_dim, hidden_dim)
        self.out = nn.Linear(hidden_dim, output_dim)

    def forward(self, text):
        embedded = self.embedding(text)
        pooled = embedded.mean(dim=1)
        return self.out(pooled)

    def train_model(self, train_loader, criterion, optimizer, epochs=10):
        self.train()
        for epoch in range(epochs):
            for text, labels in train_loader:
                optimizer.zero_grad()
                predictions = self(text).squeeze(1)
                loss = criterion(predictions, labels)
                loss.backward()
                optimizer.step()

    def predict(self, text):
        self.eval()
        with torch.no_grad():
            predictions = self(text).squeeze(1)
            return torch.round(torch.sigmoid(predictions))

def build_vocab(documents, tokenizer):
    def yield_tokens(data_iter):
        for text in data_iter:
            yield tokenizer(text)
    
    vocab = build_vocab_from_iterator(yield_tokens(documents), specials=['<pad>'])
    vocab.set_default_index(vocab['<pad>'])
    return vocab

def preprocess_data(documents, labels, vocab, tokenizer, max_length=120):
    dataset = DocumentDataset(documents, labels, vocab=vocab, tokenizer=tokenizer, max_length=max_length)
    return dataset
