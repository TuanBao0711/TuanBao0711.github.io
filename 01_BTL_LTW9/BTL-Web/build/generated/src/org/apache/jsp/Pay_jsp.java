package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class Pay_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>Thanh toán</title>\n");
      out.write("        <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\" integrity=\"sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk\" crossorigin=\"anonymous\">\n");
      out.write("        <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" integrity=\"sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI\" crossorigin=\"anonymous\"></script>\n");
      out.write("        <script src=\"https://code.jquery.com/jquery-3.5.1.slim.min.js\" integrity=\"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj\" crossorigin=\"anonymous\"></script>\n");
      out.write("        <script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js\" integrity=\"sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo\" crossorigin=\"anonymous\"></script>\n");
      out.write("\n");
      out.write("        <style>\n");
      out.write("            .btn-group-vertical>.btn:not(:first-child),\n");
      out.write(".btn-group-vertical>.btn-group:not(:first-child) {\n");
      out.write("margin-top: 0;\n");
      out.write("}\n");
      out.write("        </style>\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        <section>\n");
      out.write("  <div class=\"d-flex justify-content-between align-items-center mb-5\">\n");
      out.write("    <div class=\"d-flex flex-row align-items-center\">\n");
      out.write("      <h4 class=\"text-uppercase mt-1\">Eligible</h4>\n");
      out.write("      <span class=\"ms-2 me-3\">Thanh toán</span>\n");
      out.write("    </div>\n");
      out.write("    <a href=\"product\">Cancel and return to the website</a>\n");
      out.write("  </div>\n");
      out.write("\n");
      out.write("  <div class=\"row\">\n");
      out.write("    <div class=\"col-md-7 col-lg-7 col-xl-6 mb-4 mb-md-0\">\n");
      out.write("      <h5 class=\"mb-0 text-success\">$85.00</h5>\n");
      out.write("      <h5 class=\"mb-3\">Diabites Pump & Supplies</h5>\n");
      out.write("      <div>\n");
      out.write("        <div class=\"d-flex justify-content-between\">\n");
      out.write("          <div class=\"d-flex flex-row mt-1\">\n");
      out.write("            <h6>Insurance Responsibility</h6>\n");
      out.write("            <h6 class=\"fw-bold text-success ms-1\">$71.76</h6>\n");
      out.write("          </div>\n");
      out.write("          <div class=\"d-flex flex-row align-items-center text-primary\">\n");
      out.write("            <span class=\"ms-1\">Add Insurer card</span>\n");
      out.write("          </div>\n");
      out.write("        </div>\n");
      out.write("        <p>\n");
      out.write("          Insurance claim and all neccessary dependencies will be submitted to your\n");
      out.write("          insurer for the covered portion of this order.\n");
      out.write("        </p>\n");
      out.write("        <div class=\"p-2 d-flex justify-content-between align-items-center\" style=\"background-color: #eee;\">\n");
      out.write("          <span>Aetna - Open Access</span>\n");
      out.write("          <span>Aetna - OAP</span>\n");
      out.write("        </div>\n");
      out.write("        <hr />\n");
      out.write("        <div class=\"d-flex justify-content-between align-items-center\">\n");
      out.write("          <div class=\"d-flex flex-row mt-1\">\n");
      out.write("            <h6>Patient Balance</h6>\n");
      out.write("            <h6 class=\"fw-bold text-success ms-1\">$13.24</h6>\n");
      out.write("          </div>\n");
      out.write("          <div class=\"d-flex flex-row align-items-center text-primary\">\n");
      out.write("            <span class=\"ms-1\">Add Payment card</span>\n");
      out.write("          </div>\n");
      out.write("        </div>\n");
      out.write("        <p>\n");
      out.write("          Insurance claim and all neccessary dependencies will be submitted to your\n");
      out.write("          insurer for the covered portion of this order.\n");
      out.write("        </p>\n");
      out.write("        <div class=\"d-flex flex-column mb-3\">\n");
      out.write("          <div class=\"btn-group-vertical\" role=\"group\" aria-label=\"Vertical button group\">\n");
      out.write("            <input type=\"radio\" class=\"btn-check\" name=\"options\" id=\"option1\" autocomplete=\"off\" />\n");
      out.write("            <label class=\"btn btn-outline-primary btn-lg\" for=\"option1\">\n");
      out.write("              <div class=\"d-flex justify-content-between\">\n");
      out.write("                <span>VISA </span>\n");
      out.write("                <span>**** 5436</span>\n");
      out.write("              </div>\n");
      out.write("            </label>\n");
      out.write("\n");
      out.write("            <input type=\"radio\" class=\"btn-check\" name=\"options\" id=\"option2\" autocomplete=\"off\" checked />\n");
      out.write("            <label class=\"btn btn-outline-primary btn-lg\" for=\"option2\">\n");
      out.write("              <div class=\"d-flex justify-content-between\">\n");
      out.write("                <span>MASTER CARD </span>\n");
      out.write("                <span>**** 5038</span>\n");
      out.write("              </div>\n");
      out.write("            </label>\n");
      out.write("          </div>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"btn btn-success btn-lg btn-block\">Proceed to payment</div>\n");
      out.write("      </div>\n");
      out.write("    </div>\n");
      out.write("    <div class=\"col-md-5 col-lg-4 col-xl-4 offset-lg-1 offset-xl-2\">\n");
      out.write("      <div class=\"p-3\" style=\"background-color: #eee;\">\n");
      out.write("        <span class=\"fw-bold\">Order Recap</span>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>contracted Price</span> <span>$186.86</span>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Amount Deductible</span> <span>$0.0</span>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Coinsurance(0%)</span> <span>+ $0.0</span>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Copayment </span> <span>+ 40.00</span>\n");
      out.write("        </div>\n");
      out.write("        <hr />\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span class=\"lh-sm\">Total Deductible,<br />\n");
      out.write("            Coinsurance and copay\n");
      out.write("          </span>\n");
      out.write("          <span>$40.00</span>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span class=\"lh-sm\">Maximum out-of-pocket <br />\n");
      out.write("            on insurance policy</span>\n");
      out.write("          <span>$40.00</span>\n");
      out.write("        </div>\n");
      out.write("        <hr />\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Insurance Responsibility </span> <span>$71.76</span>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Patient Balance </span> <span>$13.24</span>\n");
      out.write("        </div>\n");
      out.write("        <hr />\n");
      out.write("        <div class=\"d-flex justify-content-between mt-2\">\n");
      out.write("          <span>Total </span> <span class=\"text-success\">$85.00</span>\n");
      out.write("        </div>\n");
      out.write("      </div>\n");
      out.write("    </div>\n");
      out.write("  </div>\n");
      out.write("</section>\n");
      out.write("\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
