<%-- 
    Document   : Left
    Created on : Apr 24, 2022, 10:40:39 PM
    Author     : b19dc
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<div class="col-sm-3">
                    <div class="card bg-light mb-3">
                        <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i> Categories</div>
                        <ul class="list-group category_block">
                            <c:forEach items="${listC}" var="o">
                                <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="category?cid=${o.cid}">${o.cname}</a></li>
                            </c:forEach>
                        </ul>
                    </div>
                     <div class="card bg-light mb-3">
                        <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i>Color</div>
                        <ul class="list-group category_block">
                            
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="#">ĐEN</a></li>
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="#">NÂU</a></li>
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="#">BẠC</a></li>
                          
                        </ul>
                    </div>
<!--                    <div class="card bg-light mb-3">
                        <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i>Price</div>
                        <ul class="list-group category_block">
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="category?cid=${o.cid}">DUOI $20</a></li>
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="category?cid=${o.cid}">$20 DEN $50</a></li>
                            <li class="list-group-item text-white ${tag == o.cid ? "active" : ""}"><a href="category?cid=${o.cid}">TREN $50</a></li>

                        </ul>
                   </div>-->
                    <div class="card bg-light mb-3">
                        <div class="card-header bg-success text-white text-uppercase">Last product</div>
                        <div class="card-body">
                            <img class="img-fluid" src="${p.image}" />
                            <h5 class="card-title">${p.name}</h5>
                            <p class="card-text">${p.title}</p>
                            <p class="bloc_left_price">${p.price} $</p>
                        </div>
                    </div>
                </div>
                        
 