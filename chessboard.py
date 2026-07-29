import matplotlib.pyplot as plt

def draw_chessboard():
    size = 8
    fig, ax = plt.subplots(figsize=(6,6))

    # Dessiner les cases
    for row in range(size):
        for col in range(size):
            # Couleur alternée
            color = "white" if (row + col) % 2 == 0 else "gray"
            rect = plt.Rectangle((col, row), 1, 1, facecolor=color, edgecolor="black")
            ax.add_patch(rect)
            # Texte au centre de la case
            ax.text(col + 0.5, row + 0.5, f"[{row}][{col}]",
                    ha="center", va="center", fontsize=8)

    # Ajustements
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)

     # Définir exactement 8 ticks et 8 labels
    ax.set_xticks([i+0.5 for i in range(size)])
    ax.set_xticklabels([str(i+1) for i in range(size)])

    ax.set_yticks([i+0.5 for i in range(size)])
    ax.set_yticklabels([str(size-i) for i in range(size)])

    ax.set_aspect("equal")
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    draw_chessboard()
