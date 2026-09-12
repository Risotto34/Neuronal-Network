import numpy as np
import matplotlib.pyplot as plt


def generate_handrawn_circle(
    path: str,
    dimensions: tuple[int, int] = (500, 500),
    center: tuple[int, int] = (250, 250),
    radius: int = 50,
    points: int = 100,
    noise: float = 0.0,
    linewidth: float = 1,
) -> None:

    # angles
    theta = np.linspace(0, 2 * np.pi, points)

    # random noise
    random_noise = np.random.normal(0, noise, points)
    r = radius + random_noise

    # coordinates
    x = center[0] + r * np.cos(theta)
    y = center[1] + r * np.sin(theta)

    # canvas
    fig, ax = plt.subplots(figsize=(dimensions[0] / 100, dimensions[1] / 100), dpi=100)

    ax.plot(x, y, "k", linewidth=linewidth)

    # set limits and remove axes
    ax.set_xlim(0, dimensions[0])
    ax.set_ylim(0, dimensions[1])
    ax.axis("off")

    # export
    fig.savefig(path, bbox_inches=None, pad_inches=0)

    plt.close(fig)


def generate_random_handrawn_circle(
    path: str,
    dimensions: tuple[int, int] = (500, 500),
) -> None:

    radius = np.random.randint(10, min(dimensions) // 2)
    center = (
        np.random.randint(radius, dimensions[0] - radius),
        np.random.randint(radius, dimensions[1] - radius),
    )
    points = np.random.randint(10, 20)
    noise = np.random.uniform(0.2, 5)
    linewidth = np.random.uniform(1, 5)

    generate_handrawn_circle(
        path=path,
        dimensions=dimensions,
        center=center,
        radius=radius,
        points=points,
        noise=noise,
        linewidth=linewidth,
    )
