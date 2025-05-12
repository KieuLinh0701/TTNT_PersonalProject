# TTNT_PersonalProject
 
## 1.	Mục tiêu:
    Mục tiêu của dự án là:
    - Nắm vững kiến thức cơ bản về các thuật toán tìm kiếm thông qua môn học Trí tuệ Nhân tạo.  
    - Hiểu rõ cách thức hoạt động của các thuật toán này và cách áp dụng chúng vào bài toán thực tế 8-puzzle.  
    - Rèn luyện kỹ năng phân tích bài toán, thiết kế giải pháp tối ưu, lập trình hiệu quả, và sửa lỗi.  
    - Tạo nền tảng để áp dụng kiến thức vào việc giải quyết các bài toán phức tạp hơn trong tương lai.  

    Thuật toán tìm kiếm bao gồm các nhóm sau:
    - Uniformed Search: 
        Breadth-First Search (BFS)
        Depth-First Search (DFS)
        Uniform Cost Search (UCS)
        Iterative Deepening Search (IDS)
    - Informed Search: 
        Greedy Search
        A* Search
        Iterative Deepening A* (IDA*)
    - Local Search: 
        Simple Hill Climbing
        Steepest-Ascent Hill Climbing
        Stochastic Hill Climbing
        Simulated Annealing (SA)
        Genetic Algorithm (GA)
    - Complex Environment: 
        And-Or Search, Belief State Search
        Searching with Partial Observation
    - Constraint Satisfaction Problems (CSPS): 
        Backtracking
        Backtracking With Forward Checking
    - Reinforcement Learning: 
        Q-Learning
        Deep Q Network (DQN)
        SARSA (State-Action-Reward-State-Action)
        Policy-Gradient

## 2. Nội dung
### 2.1. Các thuật toán Tìm kiếm không có thông tin
#### 2.1.1 Thành phần chính của bài toán tìm kiếm
    -	Trạng thái khởi đầu (Start State): Trạng thái ban đầu từ đó bắt đầu tìm kiếm.
    -	Trạng thái đích (Goal State): Trạng thái cần đạt được để giải bài toán.
    -	Không gian trạng thái (State Space): Tập hợp tất cả các trạng thái có thể đạt được từ trạng thái khởi đầu.
    -	Chi phí (Cost): Chi phí của mỗi bước di chuyển. (Có thể là cố định (BFS, DFS, IDS) hoặc thay đổi (UCS)).
    -	Cấu trúc dữ liệu: Dùng để quản lý các trạng thái cần mở rộng:
        o	Hàng đợi (BFS).
        o	Ngăn xếp (DFS, IDS).
        o	Hàng đợi ưu tiên (UCS).
    -	Đường đi (Path): Một chuỗi các trạng thái từ trạng thái khởi đầu đến trạng thái đích.
#### 2.1.2. Hình ảnh gif của từng thuật toán khi áp dụng lên trò chơi 

| ![GIF 1](gif/bfs.gif) | ![GIF 2](gif/dfs.gif) | ![GIF 3](gif/ucs.gif) | ![GIF 4](gif/ids.gif) |
|----------------------------|----------------------------|----------------------------|----------------------------|
| **Thuật toán BFS**                  | **Thuật toán DFS**                  | **Thuật toán UCS**                  | **Thuật toán IDS**                  |
#### 2.1.3. Nhận xét về hiệu suất của các thuật toán khi áp dụng lên trò chơi 8 ô chữ  

| Thuật toán | Tính đầy đủ | Tối ưu | Thời gian | Không gian	 | Nhận xét |
|-------|-------|-------|-------|-------|-------|
| BFS | Có | Có | $O(b^d)$ | $O(b^d)$ | Bộ nhớ tốn kém, nhưng đảm bảo |
| DFS | Không | Không | $O(b^m)$ | $O(bm)$ | Nhanh, nhưng dễ bị lặp hoặc lạc |
| UCS | Có | Có | $O(b^d)$ | $O(b^d)$ | Tốt khi chi phí bước không đều |
| IDS | Có | Có | $O(b^d)$ | $O(bd)$ | 	Hiệu quả hơn BFS về bộ nhớ |
