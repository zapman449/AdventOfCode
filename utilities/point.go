package utilities

type Point struct {
	x int64
	y int64
}

func NewPoint(x, y int64) Point {
	return Point{x,y}
}

func (p Point) Up() Point {
	return Point{p.x, p.y+1}
}
func (p Point) North() Point {
	return p.Up()
}

func (p Point) Down() Point {
	return Point{p.x, p.y-1}
}
func (p Point) South() Point {
	return p.Down()
}

func (p Point) Left() Point {
	return Point{p.x-1, p.y}
}
func (p Point) West() Point {
	return p.Left()
}

func (p Point) Right() Point {
	return Point{p.x+1, p.y}
}
func (p Point) East() Point {
	return p.Right()
}
