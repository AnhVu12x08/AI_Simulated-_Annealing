## Thuật toán Luyện kim (Simulated annealing)

Thuật toán luyện kim (Simulated annealing - SA) là một kỹ thuật tối ưu hóa được giới thiệu bởi Kirkpatrick và cộng sự vào năm 1983 để giải quyết bài toán Người bán hàng du lịch (Travelling Salesman Problem - TSP). 

**Nguồn gốc và nguyên lý:**

SA dựa trên quá trình tôi luyện được sử dụng trong luyện kim, nơi kim loại được đun nóng nhanh đến nhiệt độ cao rồi sau đó được làm nguội dần. Ở nhiệt độ cao, các nguyên tử di chuyển nhanh chóng, và khi nhiệt độ giảm, động năng của chúng cũng giảm. Vào cuối quá trình tôi luyện, các nguyên tử rơi vào trạng thái có trật tự hơn, và vật liệu trở nên dễ uốn hơn và dễ xử lý hơn.

Tương tự, trong SA, quá trình tìm kiếm bắt đầu ở trạng thái năng lượng cao (một trạng thái ban đầu) và giảm dần nhiệt độ (một tham số điều khiển) cho đến khi nó đạt đến trạng thái năng lượng tối thiểu (giải pháp tối ưu). 

**Cách thức hoạt động:**

1. **Khởi tạo:** Bắt đầu với một trạng thái ngẫu nhiên (tuyến đường ban đầu) và một nhiệt độ cao.
2. **Tạo láng giềng:**  Tạo ra một trạng thái láng giềng (tuyến đường mới) gần với trạng thái hiện tại. 
3. **Chấp nhận:**  Chấp nhận trạng thái mới với một xác suất dựa trên sự thay đổi năng lượng và nhiệt độ hiện tại.
4. **Làm mát:** Giảm nhiệt độ theo một tốc độ làm mát nhất định. 
5. **Lặp lại:** Tiếp tục các bước 2-4 cho đến khi đạt đến nhiệt độ tối thiểu hoặc khi tìm thấy giải pháp tối ưu.

**Ưu điểm:**

* Khả năng thoát khỏi cực tiểu cục bộ (local minima) và hội tụ đến cực tiểu toàn cục (global minimum).
* Ứng dụng rộng rãi trong nhiều vấn đề tối ưu hóa khác nhau.

**Nhược điểm:**

* Yêu cầu cài đặt các tham số (nhiệt độ ban đầu, tốc độ làm mát, nhiệt độ tối thiểu) phù hợp với bài toán.
* Có thể mất nhiều thời gian để hội tụ, đặc biệt với các vấn đề phức tạp.

**Ứng dụng:**

SA đã được áp dụng thành công vào nhiều vấn đề tối ưu hóa, chẳng hạn như:

* Bài toán người bán hàng du lịch
* Phân vùng đồ thị
* Lập lịch cho các công việc (Job shop scheduling)
* Tối ưu hóa mạng nơ-ron

**Kết luận:**

SA là một kỹ thuật tối ưu hóa mạnh mẽ và linh hoạt có thể được sử dụng để giải quyết nhiều vấn đề khác nhau. Nó cung cấp một cách tiếp cận hiệu quả để khám phá không gian giải pháp và thoát khỏi cực tiểu cục bộ, làm cho nó trở thành một công cụ hữu ích cho các nhà nghiên cứu và các chuyên gia trong nhiều lĩnh vực khác nhau.

**So sánh với thuật toán tìm kiếm leo đồi ngẫu nhiên:**

SA có thể được xem là phiên bản phát triển của thuật toán tìm kiếm leo đồi ngẫu nhiên. Cả hai thuật toán đều khám phá không gian giải pháp bằng cách di chuyển đến các trạng thái láng giềng, nhưng SA sử dụng nhiệt độ để cho phép nó chấp nhận các trạng thái kém hơn với xác suất nhất định, giúp nó thoát khỏi cực tiểu cục bộ.  Thuật toán tìm kiếm leo đồi ngẫu nhiên chỉ di chuyển đến các trạng thái tốt hơn, có thể khiến nó bị mắc kẹt trong cực tiểu cục bộ.

![image](https://github.com/user-attachments/assets/615f9539-f68a-4123-b05f-1aad6b4a1a7e)

### Ví dụ về tìm giá trị nhỏ nhất của phương trình trên tọa độ
![image](https://github.com/user-attachments/assets/3cb02382-636b-4deb-ab89-575513710a6a)

### Ví dụ về sử dụng thuật toán luyện kim giải quyết bài toán Travelling Saleman Problem
![image](https://github.com/user-attachments/assets/2c65f15a-6cd0-404e-9542-642f53074318)
