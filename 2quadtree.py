import numpy as np
from PIL import Image, ImageDraw

MAX_DEPTH = 8
DETAIL_THRESHOLD = 13

def average_color(img):
    arr = np.asarray(img)
    return tuple(map(int, np.mean(arr, axis=(0, 1))))

def detail_from_hist(hist):
    def std_dev(channel): 
        total = sum(channel)
        if total == 0: return 0
        mean = sum(i * val for i, val in enumerate(channel)) / total
        return (sum(val * (i - mean) ** 2 for i, val in enumerate(channel)) / total) ** 0.5
    r, g, b = std_dev(hist[:256]), std_dev(hist[256:512]), std_dev(hist[512:768])
    return 0.2989 * r + 0.5870 * g + 0.1140 * b

class Quadrant:
    def __init__(self, img, bbox, depth):
        self.bbox, self.depth = bbox, depth
        self.children, self.leaf = None, False
        region = img.crop(bbox)
        self.colour = average_color(region)
        self.detail = detail_from_hist(region.histogram())

    def split(self, img):
        l, t, r, b = self.bbox
        mx, my = (l + r) / 2, (t + b) / 2
        coords = [(l, t, mx, my), (mx, t, r, my), (l, my, mx, b), (mx, my, r, b)]
        self.children = [Quadrant(img, c, self.depth + 1) for c in coords]

class QuadTree:
    def __init__(self, img):
        self.width, self.height = img.size
        self.max_depth = 0
        self.root = Quadrant(img, (0, 0, self.width, self.height), 0)
        self._build(self.root, img)

    def _build(self, node, img):
        if node.depth >= MAX_DEPTH or node.detail <= DETAIL_THRESHOLD:
            node.leaf = True
            self.max_depth = max(self.max_depth, node.depth)
            return
        node.split(img)
        for child in node.children:
            self._build(child, img)

    def _collect_leaves(self, node, depth, leaves):
        if node.leaf or node.depth == depth:
            leaves.append(node)
        elif node.children:
            for child in node.children:
                self._collect_leaves(child, depth, leaves)

    def create_image(self, depth, show_lines=False):
        img = Image.new("RGB", (self.width, self.height))
        draw = ImageDraw.Draw(img)
        leaves = []
        self._collect_leaves(self.root, depth, leaves)
        for q in leaves:
            draw.rectangle(q.bbox, fill=q.colour, outline=(0, 0, 0) if show_lines else None)
        return img

    def create_gif(self, filename, duration=1000, loop=0, show_lines=False):
        frames = [self.create_image(d, show_lines) for d in range(self.max_depth + 1)]
        frames += [frames[-1]] * 4
        frames[0].save(filename, save_all=True, append_images=frames[1:], duration=duration, loop=loop)

if __name__ == '__main__':
    img_path = r"C:\Users\vegu2\Desktop\New folder (3)\pic3.jpg"
    img = Image.open(img_path)
    quadtree = QuadTree(img)
    final_img = quadtree.create_image(depth=7, show_lines=False)
    final_img.show()
    final_img.save("img_quadtree.jpg")
    quadtree.create_gif("img_quadtree1.gif", show_lines=True)
