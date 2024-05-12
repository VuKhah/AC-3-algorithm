TRÒ CHƠI SUDOKU
	3.1. Giới thiệu trò chơi
        Sudoku là một trò chơi giải đố logic sử dụng các con số vô cùng phổ biến và được yêu thích trên toàn thế giới, có đa dạng câu đố từ dễ đến khó. 
      Trò chơi này không đòi hỏi kiến thức toán học cao siêu mà chỉ cần sự tập trung, tư duy logic và óc suy luận nhạy bén để giải mã những ô số bí ẩn. 
      Sudoku bao gồm một lưới 9x9, được chia thành 9 hình vuông nhỏ 3x3. 
      Mục tiêu của trò chơi là điền các số từ 1 đến 9 vào lưới sao cho mỗi hàng, mỗi cột và mỗi hình vuông 3x3 đều chứa tất cả các số từ 1 đến 9 mà không lặp lại. 

      Được rồi, ở đây chúng tôi không đủ nghị lực để giải mã một ván chơi Sudoku. Hãy để Constraint Propagation giúp chúng ta làm điều đó.
	3.2. Sử dụng AC-3 giải quyết bài toán Sudoku
        Trò chơi Sudoku có thể được xem như một bài toán CSP có 81 biến số tương đường với 81 ô trên bảng Sudoku. Với mỗi biến số có một miền giá trị từ 1 đến 9. 
      Đối với một bảng Sudoku tiêu chuẩn 9x9, có tổng cộng: 9 AllDifferent Constraints cho các hàng, 9 AllDifferent Constraints cho các cột và 9 AllDifferent Constraints cho các hình vuông 3x3. 
      Thuật toán AC-3 có thể được sử dụng để chuyển đổi các ràng buộc Alldiff thành các ràng buộc nhị phân. 
      Ví dụ, một ràng buộc Alldiff cho một hàng hoặc một cột có thể được chia nhỏ thành các ràng buộc Diff giữa mỗi cặp biến số trong hàng hoặc cột đó. 
      
      Một ràng buộc Alldiff có thể được biểu diễn như sau:
	      Mỗi ràng buộc Alldiff có thể được chuyển đổi thành 36 ràng buộc Diff (A,B), và với 27 Alldiff constraints trong một bảng Sudoku, điều này dẫn đến việc có tổng cộng 972 ràng buộc Diff (27 * 36). 
      Tuy nhiên, do mỗi cặp biến số có hai hướng ràng buộc (ví dụ: Diff(A,B) và Diff(B,A) là khác nhau), số lượng ràng buộc thực tế cần xem xét là 1944 (27*36*2).
	    Thuật toán AC-3 sẽ lặp đi lặp lại qua các cặp biến số này để đảm bảo tính nhất quán của cung, loại bỏ những giá trị không thỏa mãn từ miền giá trị của các biến số. 
      Quá trình này tiếp tục cho đến khi không còn giá trị nào có thể loại bỏ hoặc khi bảng Sudoku được giải quyết hoàn toàn.
