import torch
import torch.nn as nn 
import matplotlib.pyplot as plt

# Konstanta
y0 = 1
v0 = 0
m = 1
b = 3.5
k = 100

# Waktu awal, waktu latih, dan waktu uji
t_initial = torch.tensor(0.0).view(-1, 1).requires_grad_(True)
t_train = torch.linspace(0, 3, 300).view(-1, 1).requires_grad_(True)
t_test = torch.linspace(0, 3, 300).view(-1, 1)

# Arsitektur neural network
class PINNs(nn.Module):
    def __init__(self, n_hidden):
        super(PINNs, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(1, n_hidden),
            nn.Tanh(),
            nn.Linear(n_hidden, n_hidden),
            nn.Tanh(),
            nn.Linear(n_hidden, 1)
        )
    
    def forward(self, t):
        return self.net(t)

model = PINNs(n_hidden=20)
learning_rate = 0.01
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Turunan
def derivative(num, den):
    return torch.autograd.grad(num, den, torch.ones_like(num), create_graph=True)[0]

# Training
num_epochs = 5000
for epoch in range(num_epochs + 1):
    optimizer.zero_grad()

    y0_pred = model(t_initial)
    loss1 = (torch.squeeze(y0_pred) - y0)**2

    v0_pred = derivative(y0_pred, t_initial)
    loss2 = (torch.squeeze(v0_pred) - v0)**2

    y = model(t_train)
    v = derivative(y, t_train)
    a = derivative(v, t_train)
    loss3 = torch.mean((m*a + b*v + k*y)**2)

    loss = loss1 + 1e-2*loss2 + 1e-2*loss3

    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f'Epoch: {epoch}/{num_epochs} ===> Loss: {loss.item():.6f}')

# Visualization
plt.plot(t_test.detach().numpy(), model(t_test).detach().numpy(), label="Prediction")
plt.plot(t_train.detach().numpy(), model(t_train).detach().numpy(), label="Training")
plt.title("Damped Oscillation using PINNs")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.legend()
plt.grid()
plt.show()
