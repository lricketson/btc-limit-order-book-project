import torch
from torch.utils.data import Dataset, DataLoader


class LOBDataset(Dataset):
    def __init__(self, df, sequence_length=100):
        # We separate the features (X) from the target (y)
        # Assuming 'target' is the final column you created
        self.X = df.drop(columns=["target"]).values  # Convert to 2D numpy array
        self.y = df["target"].values
        self.seq_len = sequence_length

    def __len__(self):
        # We can't start a sequence if there aren't enough rows left
        return len(self.X) - self.seq_len

    def __getitem__(self, idx):

        pass
