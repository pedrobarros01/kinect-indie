
class GameService: 
    @classmethod
    def pulou(cls, points_detect_minimum: tuple[int, int], line_points: list[tuple[int, int]]) -> bool:
        _, y_min_player = points_detect_minimum
        _, y_start_line = line_points[0]
        _, y_end_line = line_points[1]
        if y_min_player < y_start_line and y_min_player < y_end_line:
            return True
        return False
    

    @classmethod
    def mover(cls, points_detect_minimum: tuple[int, int],points_detect_max: tuple[int, int], quad_points: list[tuple[int, int]]) -> bool:
        x_min_player, y_min_player = points_detect_minimum
        x_max_player, y_max_player = points_detect_max
        x_start_quad, y_start_quad = quad_points[0]
        x_end_quad, y_end_quad = quad_points[1]
        half_y_max_player = y_max_player // 2
        if (x_min_player >= x_start_quad and x_min_player <= x_end_quad) or (x_max_player >= x_start_quad and x_max_player <= x_end_quad):
            return True
        return False
    