/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package controller;

import dal.DAO;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import model.Category;
import model.Product;

/**
 *
 * @author b19dc
 */
public class CategoryServlet extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        request.setCharacterEncoding("UTF-8");
       
        
        String cateID = request.getParameter("category");
        String color = request.getParameter("color");
        String price = request.getParameter("price");
        
        if (cateID==null) cateID = " 1=1 ";
        else cateID = " cateID =" + " " + cateID + " ";
        if (color==null) color = " and 1=1  ";
        else color = " and title= " + " N'" + color + "' ";
        if (price==null) price = " ";
        else {
            if (price.equals("1")){
                price = " and price<200";
            }
            else if (price.equals("3")){
                price = " and price>500";
            }
            else{
                price = " and price>=200 and price<=500";
            }
        }
        String sql = "Select *from Product where "+ cateID + color + price;
        
//        String bede = cateID + " " + color + " " + price;

        request.setAttribute("message", sql);
        DAO dao = new DAO();
        List<Product> list = dao.getProductByFilter(cateID,color,price);
        List<Category> listC = dao.getAllCategories();
        Product d = dao.getLast();   
        request.setAttribute("listC", listC);
        request.setAttribute("listP", list);
        request.setAttribute("p", d);
        request.setAttribute("tag", cateID);
        request.getRequestDispatcher("Home.jsp").forward(request, response);
//        request.getRequestDispatcher("vd.jsp").forward(request, response);
//        String cateID = request.getParameter("cid");
//        // da lay duoc san pham
//        DAO dao = new DAO();
//        List<Product> list = dao.getProductByCategory(cateID);
//        List<Category> listC = dao.getAllCategories();
//        Product d = dao.getLast();   
//        request.setAttribute("listC", listC);
//        request.setAttribute("listP", list);
//        request.setAttribute("p", d);
//        request.setAttribute("tag", cateID);
//        request.getRequestDispatcher("Home.jsp").forward(request, response);
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
