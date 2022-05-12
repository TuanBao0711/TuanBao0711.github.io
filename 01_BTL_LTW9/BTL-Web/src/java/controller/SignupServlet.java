/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package controller;

import dal.DAO;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import model.Account;

/**
 *
 * @author b19dc
 */
public class SignupServlet extends HttpServlet {

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
        String name = request.getParameter("name1");
        String user = request.getParameter("user1");
        String pass = request.getParameter("pass1");
        String re_pass = request.getParameter("repass");
        String pos = request.getParameter("pos");
        int x=0;
        if (pos.equals("sell")) x=1; 
        
        if (!pass.equals(re_pass)){
           request.setAttribute("message", "Mật khẩu nhập lại không đúng");
           request.getRequestDispatcher("Registered.jsp").forward(request, response);
        }     
        else {
            DAO dao = new DAO();
            Account a = dao.checkAccountExit(user);
            if (a!=null){
               
                request.setAttribute("message", "Tài khoản đã tồn tại ");
                request.getRequestDispatcher("Registered.jsp").forward(request, response);
            }
            else {
                dao.insert(name,user, pass,x);
                request.setAttribute("message", "Đăng kí thành công!!!  "+ x);
                request.getRequestDispatcher("Registered.jsp").forward(request, response);
            }
        }
//        else {
//             DAO dao = new DAO();
//             Account a = dao.checkAccountExit(user);
//             if (a==null){
//                 dao.insert(user, pass);
//                 response.sendRedirect("product");
//             }else {
//                 // day ve trang login
//                 response.sendRedirect("Login.jsp");
//             }
//        }
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
