<%-- 
    Document   : cart
    Created on : Apr 29, 2022, 2:34:10 PM
    Author     : b19dc
--%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Giỏ hàng</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>


        <style>
          
        </style>
    </head>
    <body>
      <section class="h-100" style="background-color: #eee;">
  <div class="container h-100 py-5">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-10">

        <div class="d-flex justify-content-between align-items-center mb-4">
          <h3 class="fw-normal mb-0 text-black">Shopping Cart</h3>
          <div>
            <p class="mb-0"><span class="text-muted"></span><a style="font-size: 35px; text-decoration : none" href="#!" class="text-body">Total Money: $${cart.getTotalMoney()}<i
                  class="fas fa-angle-down mt-1"></i></a></p>
          </div>
        </div>
        <c:if test="${cart.getSize() == 0}">
            <h3 class="fw-normal mb-0 text-black">Chưa có sản phẩm nào trong giỏ hàng</h3>              
        </c:if>
       
        <c:set var="o" value="${requestScope.cart}"/>
        <c:set var="tt" value="0"/>
        <c:forEach items="${o.items}" var="i">
        <div class="card rounded-3 mb-4">
          <div class="card-body p-4">
            <div class="row d-flex justify-content-between align-items-center">
              <div class="col-md-2 col-lg-2 col-xl-2">
                <img
                  src="${i.product.image}"
                  class="img-fluid rounded-3" alt="Cotton T-shirt">
              </div>
              <div class="col-md-3 col-lg-3 col-xl-3">
                <p class="lead fw-normal mb-2">${i.product.name}</p>
                <p><span class="text-muted">Màu : </span>${i.product.title}</p>
              </div>
            <div>
                <button><a href="process?num=-1&id=${i.product.id}">-</a></button>
                ${i.quantity}
                <button><a href="process?num=1&id=${i.product.id}">+</a></button>
            </div>
              <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                <h5 class="mb-0">$${i.product.price}</h5>
              </div>
<!--              <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                <a href="#!" class="text-danger"><i class="fas fa-trash fa-lg"></i></a>
              </div>-->
            <form action="process" method="post">
                            <input type="hidden" name="id" value="${i.product.id}"/>
                            <input type="submit" value="Xóa sản phẩm"/>
                        </form>
            </div>
          </div>
        </div>
        </c:forEach>

        <br/>
        <br/>
  
        <c:if test="${cart.getSize() > 0}">
        <div class="card">
          <div class="card-body">
<!--            <form action="pay" method="post">-->
                    <a style="text-decoration : none" href="payment?totalmoney=${cart.getTotalMoney()}">
                    <input  style="background-color:blue" class="btn btn-warning btn-block btn-lg" type="submit" value="Thanh Toan"/>
                    </a>
                    <!--            </form>-->
          </div>
        </div>
        </c:if>
        
                  

        <div class="card">
          <div class="card-body">
              <button type="button" class="btn btn-warning btn-block btn-lg">
                  <a style="color:white; text-decoration : none" href="product">Tiếp tục mua sắm tại đây</a>
              </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>
    </body>
</html>
