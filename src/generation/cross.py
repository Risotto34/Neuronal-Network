import numpy as np
import matplotlib.pyplot as plt


def generate_handrawn_cross(
    path: str,
    dimensions: tuple[int, int] = (500, 500),
    center: tuple[int, int] = (250, 250),
    size: int = 50,
    length_noise: float = 0.0,
    angle_noise: float = 0.0,
    linewidth: float = 1,
) -> None:

    cx, cy = center

    # random angle of the first line
    angle = np.random.uniform(0, 2 * np.pi)

    # angle between the two lines
    angle_2 = angle + np.pi / 2 + np.random.uniform(-angle_noise, angle_noise)

    # random length for each of the 4 branches
    lengths = np.random.uniform((1 - length_noise) * size, (1 + length_noise) * size, 4)

    # first branch
    x1 = cx + lengths[0] * np.cos(angle)
    y1 = cy + lengths[0] * np.sin(angle)

    # second branch
    x2 = cx - lengths[1] * np.cos(angle)
    y2 = cy - lengths[1] * np.sin(angle)

    # third branch
    x3 = cx + lengths[2] * np.cos(angle_2)
    y3 = cy + lengths[2] * np.sin(angle_2)

    # fourth branch
    x4 = cx - lengths[3] * np.cos(angle_2)
    y4 = cy - lengths[3] * np.sin(angle_2)

    # canvas
    fig, ax = plt.subplots(figsize=(dimensions[0] / 100, dimensions[1] / 100), dpi=100)

    # draw the 4 branches independently
    ax.plot([cx, x1], [cy, y1], "k", linewidth=linewidth)
    ax.plot([cx, x2], [cy, y2], "k", linewidth=linewidth)
    ax.plot([cx, x3], [cy, y3], "k", linewidth=linewidth)
    ax.plot([cx, x4], [cy, y4], "k", linewidth=linewidth)

    ax.set_xlim(0, dimensions[0])
    ax.set_ylim(0, dimensions[1])
    ax.axis("off")

    fig.savefig(path, bbox_inches=None, pad_inches=0)

    plt.close(fig)


def generate_random_handrawn_cross(
    path: str, dimensions: tuple[int, int] = (500, 500)
) -> None:

    size = np.random.randint(10, min(dimensions) // 4)
    center = (
        np.random.randint(size, dimensions[0] - size),
        np.random.randint(size, dimensions[1] - size),
    )
    angle_noise = np.random.uniform(0, np.pi / 18)
    linewidth = np.random.uniform(1, 5)

    generate_handrawn_cross(
        path=path,
        dimensions=dimensions,
        center=center,
        size=size,
        length_noise=0.5,
        angle_noise=angle_noise,
        linewidth=linewidth,
    )
