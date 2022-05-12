<%-- 
    Document   : Pay
    Created on : Apr 30, 2022, 10:32:11 PM
    Author     : b19dc
--%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Thanh toán</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

        <style>
            .btn-group-vertical>.btn:not(:first-child),
.btn-group-vertical>.btn-group:not(:first-child) {
margin-top: 0;
}
        </style>
    </head>
    <body>
       <section>
  <div class="row">
    <div class="col-md-8 mb-4">
      <div class="card mb-4">
        <div class="card-header py-3">
          <h5 class="mb-0">Thông tin thanh toán</h5>
        </div>
        <div class="card-body">
          <form>
            <!-- 2 column grid layout with text inputs for the first and last names -->
<!--            <div class="row mb-4">
              <div class="col">
                <div class="form-outline">
                  <input type="text" id="form6Example1" class="form-control" />
                  <label class="form-label" for="form6Example1">First name</label>
                </div>
              </div>
              <div class="col">
                <div class="form-outline">
                  <input type="text" id="form6Example2" class="form-control" />
                  <label class="form-label" for="form6Example2">Last name</label>
                </div>
              </div>
            </div>-->

            <!-- Text input -->
            <div class="form-outline mb-4">
              <input type="text" id="form6Example3" class="form-control" />
              <label class="form-label" for="form6Example3">Your name</label>
            </div>

            <!-- Text input -->
            <div class="form-outline mb-4">
              <input type="text" id="form6Example4" class="form-control" />
              <label class="form-label" for="form6Example4">Address</label>
            </div>

            <!-- Email input -->
            <div class="form-outline mb-4">
              <input type="text" id="form6Example5" class="form-control" />
              <label class="form-label" for="form6Example5">Phone Number</label>
            </div>

          

            <hr class="my-4" />

            <button class="btn btn-primary btn-lg btn-block" >
                <a style="color:white;text-decoration : none"  href="TT.jsp">Phương thức thanh toán</a>
            </button>
          </form>
        </div>
      </div>
    </div>

    <div class="col-md-4 mb-4">
      <div class="card mb-4">
        <div class="card-header py-3">
          <h5 class="mb-0">Tổng tiền</h5>
        </div>
        <div class="card-body">
          <ul class="list-group list-group-flush">
            <li class="list-group-item d-flex justify-content-between align-items-center border-0 px-0 pb-0">
              Products
              <span>$${money}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center px-0">
              Phí ship
              <span>$10.0</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center border-0 px-0 mb-3">
              <div>
                <strong>Tổng tiền</strong>
                <strong>
                  <p class="mb-0">(bao gồm VAT)</p>
                </strong>
              </div>
              <span><strong>$${money+10.0}</strong></span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

    </body>
</html>
