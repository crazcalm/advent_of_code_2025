import fileinput
from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y
    
class Shape:
    def __init__(self, points):
        self.points = points
        self.wall = set()
        self._set_upper_bounds()
        self.cache = {}

    def set_wall(self):
        for _ in self:
            pass

    def shape_in_shape(self, other):
        result = True
        for point in other:
            if not self.point_in_shape(point):
                result = False
                break
        return result
        
    def point_in_shape(self, point):
        #print("start point in shape")
        if (point.x, point.y) in self.cache:
            return self.cache[(point.x, point.y)]
        
        if (point.x, point.y) in self.wall:
            self.cache[(point.x, point.y)] = True
            return True

        if point.x < self.lower_x or point.x > self.upper_x or point.y < self.lower_y or point.y > self.upper_y:
            self.cache[(point.x, point.y)] = False
            return False
        
        right_wall = False
        left_wall = False
        up_wall = False
        down_wall = False

        result = False
        y = point.y
        while y < self.upper_y:
            if (point.x, y) in self.wall:
                up_wall = True
                break
            elif self.cache.get((point.x, y)) is not None:
                self.cache[(point.x, point.y)] = self.cache[(point.x, y)]
                return self.cache[(point.x, y)]
            else:
                y += 1

        if up_wall is False:
            self.cache[(point.x, point.y)] = result
            return result
        
        y = point.y
        while y > self.lower_y:
            if (point.x, y) in self.wall:
                down_wall = True
                break

            elif self.cache.get((point.x, y)) is not None:
                self.cache[(point.x, point.y)] = self.cache[(point.x, y)]
                return self.cache[(point.x, y)]
            
            else:
                y -= 1

        if down_wall is False:
            self.cache[(point.x, point.y)] = result
            return result
    
        x = point.x
        while x < self.upper_x:
            if (x, point.y) in self.wall:
                right_wall = True
                break

            elif self.cache.get((x, point.y)) is not None:
                self.cache[(point.x, point.y)] = self.cache[(x, point.y)]
                return self.cache[(x, point.y)]
            
            else:
                x += 1

        if right_wall is False:
            self.cache[(point.x, point.y)] = result
            return result

        x = point.x
        while x > self.lower_x:
            if (x, point.y) in self.wall:
                left_wall = True
                break
            
            elif self.cache.get((x, point.y)) is not None:
                self.cache[(point.x, point.y)] = self.cache[(x, point.y)]
                return self.cache[(x, point.y)]
            
            else:
                x -= 1

        if all([up_wall, down_wall, right_wall, left_wall]):
            result = True

        #print("end point_in_shape")
        self.cache[(point.x, point.y)] = result
        return result
        
    def _set_upper_bounds(self):
        x = 0
        y = 0
        for point in self.points:
            if point.x > x:
                x = point.x
            if point.y > y:
                y = point.y

        self.upper_x = x + 1
        self.upper_y = y + 1

        min_x = x
        min_y = y

        for point in self.points:
            if point.x < min_x:
                min_x = point.x
            if point.y < min_y:
                min_y = point.y

        self.lower_x = min_x - 1
        self.lower_y = min_y - 1
        
    def __iter__(self):
        self.index = 0
        self.current = None
        self.wall = set()
        self.last_connection = False
        return self

    def __next__(self):
        if self.current:
            if (self.current.x, self.current.y) in self.wall:
                raise StopIteration

            self.wall.add((self.current.x, self.current.y))
        
        if self.current is None:
            self.current = deepcopy(self.points[self.index])
            self.index += 1

            return self.current

        if self.current == self.points[self.index]:
            self.index += 1
        
        if self.index >= len(self.points):
            self.index = 0
            self.last_connection = True
        
        if self.current.x == self.points[self.index].x:
            if self.current.y > self.points[self.index].y:
                self.current.y -= 1
            else:
                self.current.y += 1
        elif self.current.y == self.points[self.index].y:
            if self.current.x > self.points[self.index].x:
                self.current.x -= 1
            else:
                self.current.x += 1

        if self.current == self.points[0] and self.last_connection:
            raise StopIteration
        
        return self.current

    def fill_cache(self):
        pass


class ShapeV2(Shape):
    def fill_cache(self):
        for x in range(self.lower_x, self.upper_x):
            for y in range(self.lower_y, self.upper_y):
                self.point_in_shape(Point(x,y))

    
    def shape_in_shape(self, other):
        result = True
        for point in other:
            if not self.cache.get((point.x, point.y), False):
                result = False
                break
        return result


class ShapeV3(ShapeV2):
    def fill_cache(self):
        #import pdb
        #pdb.set_trace()
        print("start fill cache")
        count = len(self.wall)
        for x,y in self.wall:
            point = Point(x,y)
            while self.point_in_shape(point):
                point.y += 1
                print(f"size of cache: {len(self.cache)}")
            count -= 1
            print(f"wall points left: {count}")
            
    
def create_rectangle(p1, p2):
    x_diff = abs(p1.x - p2.x)
    y_diff = abs(p1.y - p2.y)

    p1_5 = None
    p2_5 = None
    if p1.x < p2.x:
        p1_5 = Point(p1.x + x_diff, p1.y)
    else:
        p1_5 = Point(p1.x - x_diff, p1.y)

    if p1.y < p2.y:
        p2_5 = Point(p1.x, p1.y + y_diff)
    else:
        p2_5 = Point(p1.x, p1.y - y_diff)

    return (p1, p1_5, p2, p2_5)


def main():
    points = []
    for line in fileinput.input():
        line = line.strip()
        if not line:
            break

        x, y = line.split(",")
        points.append(Point(int(x), int(y)))

    print(points)

    shape = Shape(points)
    #for point in shape:
    #    print(point)
    shape.set_wall()
    shape.fill_cache()

    
    from pprint import pprint
    pprint(shape.cache)

    largest = 0
    seen = set()
    count = 0
    data = []
    for p1 in points:
        for p2 in points:
            count += 1
            print(f"count - {count}")
            if p1 == p2:
                continue
            if (p1.x, p1.y, p2.x, p2.y) in seen:
                continue
            distance = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
            data.append((distance, p1, p2))

    data.sort(key=lambda x: x[0])

    pprint(data)

    count = len(data)
    for distance, p1, p2 in reversed(data):
        rect = Shape(points=create_rectangle(p1, p2))
        if distance > largest:
            if shape.shape_in_shape(rect):
                largest = distance
                print(f"current largest: {largest}")

            seen.add((p1.x, p1.y, p2.x, p2.y))
            seen.add((p2.x, p2.y, p1.x, p1.y))
        print(f"current_count: {count}")
        count -= 1
    print(largest)
    
if __name__ == "__main__":
    main()
