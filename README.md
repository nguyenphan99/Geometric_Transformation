# Geometric_Transformation
Bài viết giới thiệu về Geometric transformation.
Để chạy được code, ta cần chỉnh sửa biến image_path thành đường dẫn tới ảnh đầu vào, out_path thành đường dẫn tới ảnh đầu ra.
Ta có thể thay đổi tham số Ma trận biến đổi tương ứng cho từng phép biến đổi.
[TOC]

# Biến đổi hình học - Geometric transformation

##  1. Giới thiệu biến đổi hình học

Khi ta nói về biến đổi hình học, ta thường nghĩ đến gì đầu tiên? Cùng lấy ví dụ để dễ hình dung hơn. Đầu tiên ta có cuốn tập bên trái như Hình 1, làm cách nào để cuốn tập có thể có được hình dạng, vị trí, kích thước, góc cạnh giống như hình bên phải?

<p>
    <center><img src="https://scontent.fsgn3-1.fna.fbcdn.net/v/t1.0-9/76775110_2275467899411807_6181965408040386560_n.jpg?_nc_cat=111&_nc_oc=AQmtrntNKFSUUUGsPPiu1EFArfW1b49mWzkEvo3V4pWjFljsPw-eOVprDK1kXrJweBI&_nc_ht=scontent.fsgn3-1.fna&oh=721a723a7dc30b35c4cb4abb9c5945a1&oe=5E50FDEE"width=500></center>
<center> Hình 1: Ví dụ minh họa phép biến đổi hình học [2]
</p>

Từ cuốn sổ ở hình bên trái, ta cần **căn chỉnh tỉ lệ** của cuốn sổ, sau đó **tịnh tiến** đến vị trí phù hợp, cuối cùng **xoay** một góc sao cho kết quả ta được hình bên phải.

## 2. Biến đổi hình học thực chất là gì?

Vậy biến đổi hình học là gì? Một phép biến đổi hình học là bất kỳ sự lựa chọn nào của một tập hợp có một số cấu trúc hình học cho chính nó hoặc một tập hợp khác. Cụ thể, "Biến đổi hình học là một hàm có miền và phạm vi là tập hợp các điểm. Thông thường, miền và phạm vi của phép biến đổi hình học là cả R2 hoặc cả R3. Thông thường các phép biến đổi hình học phải là các hàm 1-1, do đó chúng phải có nghịch đảo." [5]

Nói 1 cách khái quát để dễ hiểu, Phép biến đổi là các phép ánh xạ tọa độ điểm hay vector thành tọa độ hay vector khác [4].

Ví dụ ta có các phép biến đổi như hình 2:

<p>
    <center><img src="https://scontent.fsgn4-1.fna.fbcdn.net/v/t1.0-9/74528893_2275467919411805_7772381734640812032_n.jpg?_nc_cat=100&_nc_oc=AQm5-gA9-OJBXH0WQuXJzO5n6DY9wC9rQUCAXQsO8XG7lGxoMzkjnzwpblp9rIV2IFs&_nc_ht=scontent.fsgn4-1.fna&oh=d586a46ea482438a0e92e65099ef90b0&oe=5E4F7C98"width=500></center>
<center> Hình 2: Một số phép biến đổi hình học [2]
</p>

## 3. Các phép Biến đổi hình học thường gặp

### a. Phép biến đổi tuyến tính - Linear Transformation

* ***Phép tỉ lệ*** - ***Scale***: thay đổi kích thước ảnh theo tỉ lệ: $x'$ = $ax$, $y'$ = $by$. Ta có thể tìm được ma trận kết hợp $a$, $b$. Khi ta nhân ma trận tỉ lệ $\bold{M}$ có kích thước $2$x$2$ cho ma trận tọa độ điểm ảnh có kích thước $2$x$1$ ta được tọa độ mới tỉ lệ đúng bằng $x'$ = $ax$, $y'$ = $by$.
  $$
  x' = ax\\y' = by\\\begin{bmatrix}x'\\y'\end{bmatrix} = \bold{M}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}a & 0\\0 & b\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
  $$

<p>
    <center><img src="E:\Beautiful_Girl_Pictures\rose_scaled.gif"width=400></center>
<center> Hình 3: Minh họa phép tỉ lệ (vùng màu đen là vùng không có điểm ảnh)
</p>

* ***Phép xoay*** - ***Rotation***:  Xét 1 điểm $x$ trên ảnh làm đại diện, xoay $x$ một góc $\theta$ - góc tính từ tọa độ $x$ ban đầu đến $x'$ sau khi đã xoay, tương tự ta cũng tìm được ma trận $\bold{M}$:
  $$
  x' = x\cos\theta - y\sin\theta\\y' = x\sin\theta + y\cos\theta\\\begin{bmatrix}x'\\y'\end{bmatrix} = \bold{M}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}\cos\theta & - \sin\theta\\\sin\theta & \cos\theta\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
  $$

  <p>
      <center><img src="E:\Beautiful_Girl_Pictures\rose_rotated.gif"width=400></center>
  <center> Hình 4: Minh họa phép xoay
  </p>

* ***Phép trượt nghiêng*** - ***Shear***: tương tự phép tỉ lệ thì phép trượt nghiêng có thể hiểu là thay đổi độ dài theo đường chéo: 

  $x'$ = $x$ + $ay$, $y'$ = $bx$ + $y$, tương tự ta cũng tìm được ma trận $\bold{M}$:
  $$
  x' = x + ay\\y' = bx+ y\\\begin{bmatrix}x'\\y'\end{bmatrix} = \bold{M}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}1 & a\\b & 1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
  $$

  <p>
      <center><img src="E:\Beautiful_Girl_Pictures\rose_sheared.gif"width=400></center>
  <center> Hình 5: Minh họa phép trượt nghiêng
  </p>

* Ngoài ra còn có các phép biến đổi lật ảnh theo trục $Ox$, lật ảnh theo trục $Oy$,...

Tổng quát công thức chung:

$\bold{X'}$ là điểm ảnh sau khi biến đổi, có tọa độ ($x', y'$)

$\bold{X}$ là điểm ảnh được biến đổi, có tọa độ ($x, y$)

$p$ là tham số - thường là ma trận $2$x$2$ ký hiệu $\bold{M}$

$f$ là hàm biến đổi.
$$
\bold{X'} = f(\bold{X};p)\  -> 
\begin{bmatrix}
   x' \\
   y'
\end{bmatrix} = \bold{M}
\begin{bmatrix}
   x \\
   y
\end{bmatrix}
$$

* Tổng kết: ta tổng hợp một số ma trận biến đổi tuyến tính:

$$
\def\arraystretch{2.0}       \begin{array}     {c:c:c}     {Scale\\ \bold{M}=     \begin{bmatrix}    	 a & 0\\   	 0 & b     \end{bmatrix}}     &     {Flip\ Oy\\ \bold{M}=    \begin{bmatrix}    	 -1 & 0\\   	 0 & -1     \end{bmatrix}}    \\ \hline    {Rotate\\ \bold{M}=     \begin{bmatrix}    \cos\theta & -\sin\theta \\  \sin\theta &  \cos\theta \\     \end{bmatrix}}     &         {Flip\  Ox\\ \bold{M}=    \begin{bmatrix}    	 -1 & 0\\   	 0 & 1     \end{bmatrix}}    \\ \hline     {Shear\\ \bold{M}=     \begin{bmatrix}  	1 & a\\  	b & 1     \end{bmatrix}} &       {Identity\\ \bold{M}=    \begin{bmatrix}    	 1 & 0\\   	 0 & 1     \end{bmatrix}}       \end{array}
$$

**Một số tính chất của phép biến đổi tuyến tính**:

* Giữ nguyên gốc tọa độ
* Đường thẳng ánh xạ thành đường thẳng
* Bảo toàn tính song song
* Tỉ lệ được giữ nguyên
* Bảo toàn tổ hợp tuyến tính (tổ hợp của các phép biến đổi tuyến tính cũng là tuyến tính)

### b. Phép tịnh tiến - Translation

Đối với phép tịnh tiến, ta có thể áp dụng tương tự như tuyến tính để tìm ma trận biến đổi $\bold{M}$ (Hình 5)? Đáp án là không thể bởi vì không có ma trận $2$x$2$ nào cho tham số phù hợp mà độc lập với $x$, $y$.

$$
x' = x +t_x\\y' = y +t_y\\\begin{bmatrix}x'\\y'\end{bmatrix} = \bold{M}\begin{bmatrix}x\\y\end{bmatrix} =\begin{bmatrix}? & ?\\? & ?\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
$$
Vì vậy, người ta suy nghĩ thay vì biếu diễn trên mặt phẳng 2 chiều ta biếu diễn trên mặt phẳng 3 chiều bằng cách thêm 1 vào tọa độ $(x, y)$ ta được hệ tọa độ đồng nhất $(x, y, 1)$, hệ số này sẽ **"độc lập"** với $x$, $y$. 

Hệ tọa độ đồng nhất được xác định bởi tỉ lệ, ta có thể hình dung bằng cách tưởng tượng rằng khi dịch chuyển một vật lại gần hoặc ra xa tầm mắt sẽ làm cho kích thước của vật thay đổi, tương đương với khoảng cách từ mắt đến vật thay đổi.
$$
\begin{bmatrix}   x \\   y\end{bmatrix} => \begin{bmatrix}   x \\   y \\   1\end{bmatrix}\stackrel{def}{=}	\begin{bmatrix}  ax \\  ay \\  a\end{bmatrix}\\\\
$$
Với hệ tọa độ đồng nhất, ta tìm được một ma trận $3$x$3$ thỏa mãn phép tịnh tiến:
$$
\begin{bmatrix}   x' \\   y' \\   1\end{bmatrix} = \bold{M}\begin{bmatrix}   x \\   y \\   1\end{bmatrix} = \begin{bmatrix}   1 & 0 & t_{x} \\   0 & 1 & t_{y} \\   0 & 0 & 1\end{bmatrix}\begin{bmatrix}   x \\   y \\   1\end{bmatrix}
$$
Và đây là kết quả ví dụ phép tịnh tiến (hình 6, 7):

<p>
    <center><img src="E:\Beautiful_Girl_Pictures\rose_translated.gif"width=400></center>
<center> Hình 6: Minh họa phép tịnh tiến
</p>

<p>
    <center><img src="https://scontent.fsgn8-1.fna.fbcdn.net/v/t1.0-9/76678962_2275468072745123_175326547912163328_n.jpg?_nc_cat=110&_nc_oc=AQmYCVd5HRkEVBCfUJG3qRCRkM7oi-FPdLj9142nIGJ5-pspVWErk3fg0XPamekwZN4&_nc_ht=scontent.fsgn8-1.fna&oh=ca2d608b15d3f6a63465aadf0758edc7&oe=5E498C83"width=400></center>
<center> Hình 7: Minh họa thêm phép tịnh tiến [2]
</p>

### c. Euclidean (rigid)

Trước khi đi vào **Euclidean**, ta có câu hỏi như sau: *liệu ta có thể sử dụng hệ tọa độ đồng nhất cho các phép biến đổi tuyến tính ở phần đầu?* Và đáp án là **có thể**. Ta có thể thay đổi ma trận $2$x$2$ thành ma trận $3$x$3$ cho các phép biến đổi tuyến tính một cách dễ dàng:
$$
\def\arraystretch{2.0}       \begin{array}     {c:c:c}     {Scale\\ \bold{M}=     \begin{bmatrix}     a & 0 & 0\\   	 0 & b & 0\\   	 0 & 0 & 1     \end{bmatrix}}     &     {Flip\ Oy\\ \bold{M}=    \begin{bmatrix}     -1 & 0 & 0\\   	 0 & -1 & 0\\   	 0 & 0 & 1     \end{bmatrix}}    \\ \hline    {Rotate\\ \bold{M}=     \begin{bmatrix}    \cos\theta & -\sin\theta & 0\\  \sin\theta &  \cos\theta & 0 \\  0 & 0 & 1     \end{bmatrix}}     &         {Flip\  Ox\\ \bold{M}=    \begin{bmatrix}     -1 & 0 & 0\\   	 0 & 1 & 0\\   	 0 & 0 & 1     \end{bmatrix}}    \\ \hline     {Shear\\ \bold{M}=     \begin{bmatrix}  	1 & a & 0\\  	b & 1 & 0\\  	0 & 0 & 1     \end{bmatrix}} &       {Identity\\ \bold{M}=    \begin{bmatrix}     1 & 0 & 0\\   	 0 & 1 & 0\\   	 0 & 0 & 1     \end{bmatrix}}       \end{array}
$$
Ta lại có thêm một câu hỏi: *sẽ như thế nào nếu ta kết hợp các phép biến đổi tuyến tính với nhau? và kết hợp các phép biến đổi tuyến tính và phép biến đổi tịnh tiến?*

**Đó chính là ý tưởng cho Euclidean: kết hợp giữa phép xoay và phép tịnh tiến.**

Tuy nhiên, *làm cách nào để kết hợp giữa xoay và tịnh tiến?* Chỉ cần **nhân** 2 ma trận của 2 phép biến đổi xoay và tịnh tiến với nhau, ta sẽ được ma trận Euclidean tương ứng. *Vậy thứ tự nhân 2 ma trận có ảnh hưởng hay không?* Nhìn vào hình 8 ta sẽ thấy được đáp án: ***Thứ tự các phép biến đổi khác nhau sẽ cho kết quả khác nhau***.

<p>
    <center><img src="https://scontent.fsgn4-1.fna.fbcdn.net/v/t1.0-9/78955029_2286757038282893_5045303309586399232_n.jpg?_nc_cat=101&_nc_ohc=ex1GwE3l9vsAQli8X3e6jd4pS4sfx8lCaWGpwlcA-QkKfTtGaW5eg_cuA&_nc_ht=scontent.fsgn4-1.fna&oh=d09e6b5cb8568704495e7dca50231c2a&oe=5E46C785"width=600></center>
<center> Hình 8: Minh họa thứ tự các phép biến đổi  [4]
</p>

Tóm lại ta có ma trận $3$x$3$ để biến đổi Euclidean:

<center>
   Euclidean = Rotation + Translation
</center>

$$
\begin{bmatrix}\cos\theta & -\sin\theta & t_x\\\sin\theta &  \cos\theta & t_y\\0 & 0 & 1\end{bmatrix}
$$

Nếu $\theta$ thay đổi thì $\cos(\theta)$, $\sin(\theta)$ cũng thay đổi theo. Nếu **tăng giá trị $\theta$ **thì đồng nghĩa với việc ảnh hay vật thể của ta sẽ **xoay một góc lớn hơn**. Như vậy sẽ như thế nào nếu ta **tăng $t_x$** thì ảnh sẽ thay đổi như thế nào? Đáp án là ảnh sẽ **dịch chuyển tịnh tiến hơn** theo trục $Ox$, tương tự đổi với $t_y$ thì ảnh sẽ **dịch chuyển tịnh tiến hơn** theo trục $Oy$.

<p>
    <center><img src="E:\Beautiful_Girl_Pictures\rose_euclidean.gif"width=400></center>
<center> Hình 9: Minh họa phép Euclidean
</p>

### d. Phép đồng dạng - Similatity

Tương tự như **Euclidean**, phép đồng dạng là **sự kết hợp giữa Euclidean** và tỉ lệ chuẩn - **Uniform scale.**

Ta có thể tìm được ma trận biến đổi dễ dàng bằng mẹo lấy ma trận biến đổi của Euclidean, rồi lấy các phần tử trong ma trận vừa được mà có liên quan đến phép tỉ lệ để nhân với tỉ lệ $s$ :

<center>
   Similarity = Rotation + Translation + Uniform Scale
</center>

$$
\begin{bmatrix}s*\cos\theta & s*(-\sin\theta) & t_x\\s*\sin\theta &  s*\cos\theta & t_y\\0 & 0 & 1\end{bmatrix}
$$

Nếu ta **tăng $s$** có nghĩa ta đang tăng tham số của phép biến đổi tỉ lệ, vì vậy ảnh sẽ **tăng kích thước**. Nếu ta **tăng $\theta$** thì tương đương với việc ảnh sẽ **xoay một góc lớn hơn**, tương tự với $t_x$ và $t_y$ đã nói ở phép Euclidean.

<p>
    <center><img src="E:\Beautiful_Girl_Pictures\rose_similarity.gif"width=400></center>
<center> Hình 10: Minh họa phép đồng dạng
</p>

### e. Biến đổi Affine - Affine transform

Phép biến đổi Affine là **sự kết hợp giữa phép đồng dạng và phép trượt nghiêng**.

Ta có thể nhận được ma trận biến đổi bằng cách tương tự như ở phép đồng dạng, lấy ma trận phép biến đổi đồng dạng và kết hợp với phép cắt xéo: ta lấy các phần tử liên quan đến phép cắt xéo trong ma trận nhân với ma trận biến đổi cắt xéo. Sau cùng ta được ma trận biến đổi Affine:

<center>
    Affine = Rotation + Translation + Unform Scale + Shear
</center>

$$
\begin{bmatrix}s*\cos\theta + b*s*(-\sin\theta) & s*(-\sin\theta) + a*s*\cos\theta & t_x\\s*\sin\theta + b*s*\cos\theta &  s*\cos\theta+a*s*\sin\theta & t_y \\0 & 0 & 1\end{bmatrix}
$$

<p>
    <center><img src="E:\Beautiful_Girl_Pictures\rose_affine.gif"width=400></center>
<center> Hình 11: Minh họa phép affine
</p>

**Các tính chất của phép biến đổi Affine**:

* *Gốc tọa độ có thể thay đổi*
* Đường thẳng ánh xạ thành đường thẳng
* Bảo toàn tính song song
* Tỉ lệ được giữ nguyên
* Bảo toàn tổ hợp biến đổi chính nó (tổ hợp của các phép biến đổi Affine cũng là Affine)

### d. Biến đổi phối cảnh - Projective transformation

Tương tự ý tưởng với Affine transformation, Projective transformation là sự kết hợp giữa Affine transformation và Projective Wraps.

**Các tính chất của phép biến đổi phối cảnh:**

* *Gốc tọa độ có thể thay đổi*
* Đường thẳng ánh xạ thành đường thẳng
* *Tính song song có thể không được bảo toàn*
* *Tỉ lệ bị thay đổi*
* Bảo toàn tổ hợp biến đổi chính nó (tổ hợp của các phép biến đổi phối cảnh cũng là phối cảnh)

**So sánh tính chất của các phép đã học**:

<p>
    <center><img src="https://scontent.fsgn3-1.fna.fbcdn.net/v/t1.0-9/77021614_2286816281610302_65913849479430144_o.jpg?_nc_cat=106&_nc_ohc=C3TNaDT2TPMAQkYP2hS2NJpkSkALFbSaeT8zwYGGG6KsR7-9ZwxcdO0Tg&_nc_ht=scontent.fsgn3-1.fna&oh=76bac437eba37ab3a19da4b87fc48478&oe=5E476CA1"></center>

<center> Hình 12: Tổng hợp tính chất của các phép biến đổi
</p>

## 4. Tham khảo.

Có thể tham khảo code:  https://github.com/nguyenphan99/Geometric_Transformation/blob/master/transform.py 

[1] 16-385 Computer Vision, Spring 2019:  http://www.cs.cmu.edu/~16385/ 

[2]  Đại học Carnegie Mellon: http://www.cs.cmu.edu/~16385/lectures/lecture7.pdf 

[3]  Đại học Michigan Technological: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/geometry/geo-tran.html 

[4]  Đại học Bách Khoa Hà Nội: https://users.soict.hust.edu.vn/trungtt/uploads/slides/CG05_ModelingTrans.pdf 

[5]  Wikipedia:  https://en.wikipedia.org/wiki/Geometric_transformation 





