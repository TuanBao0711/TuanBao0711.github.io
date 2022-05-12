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
       <section style="background-color: #eee;">
  <div class="container py-5">
    <div class="row d-flex justify-content-center">
      <div class="col-md-8 col-lg-6 col-xl-4">
        <div class="card rounded-3">
          <div class="card-body mx-1 my-2">
            <div class="d-flex align-items-center">
              <div>
                <i class="fab fa-cc-visa fa-4x text-black pe-3"></i>
              </div>
              <div>
                <p class="d-flex flex-column mb-0">
                  <b>Phương thức thanh toán</b><span class="small text-muted">Miễn phí tiền ship với đơn hàng trên 1000$</span>
                </p>
              </div>
            </div>

            <div class="pt-3">
              <div class="d-flex flex-row pb-3">
                <div class="rounded border border-primary border-2 d-flex w-100 p-3 align-items-center"
                  style="background-color: rgba(18, 101, 241, 0.07);">
                  <div class="d-flex align-items-center pe-3">
                    <input class="form-check-input" type="radio" name="radioNoLabelX" id="radioNoLabel11"
                      value="" aria-label="..." checked />
                  </div>
                  <div class="d-flex flex-column">
                    <p class="mb-1 small text-primary">Thanh toán khi giao hàng (cod)</p>
                   
                  </div>
                </div>
              </div>

              <div class="d-flex flex-row pb-3">
                <div class="rounded border d-flex w-100 px-3 py-2 align-items-center">
                  <div class="d-flex align-items-center pe-3">
                    <input class="form-check-input" type="radio" name="radioNoLabelX" id="radioNoLabel22"
                      value="" aria-label="..." />
                  </div>
                  <div class="d-flex flex-column py-1">
                    <p class="mb-1 small text-primary">Chuyển khoản quan ngân hàng</p>
                    <div class="d-flex flex-row align-items-center">
<!--                      <h6 class="mb-0 text-primary pe-1">$</h6>-->
<!--                      <input type="text" class="form-control form-control-sm" id="numberExample"
                        style="width: 55px;" />-->
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="d-flex justify-content-between align-items-center pb-1">
              <a href="#!" class="text-muted">Go back</a>
               <button class="btn btn-primary btn-lg">
                   <a style="color:white; text-decoration : none"  href="pay">Pay amount</a>
               </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

    </body>
</html>
