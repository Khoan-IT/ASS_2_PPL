from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *


class ASTGeneration(CSELVisitor):
    # def visitProgram(self, ctx: CSELParser.ProgramContext):
    #     return Program([VarDecl(Id(ctx.ID().getText()), [], NoneType(), None)])
    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        #decl: List[Decl]
        decl = []
        for declare in ctx.declares():
            decl+= self.visit(ctx.declares())
        return  Program(decl)

    def visitDeclares(self, ctx:CSELParser.DeclareContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        elif ctx.function_declare():
            return self.visit(ctx.function_declare())
    # Visit a parse tree produced by CSELParser#var_declare.
    def visitVar_declare(self, ctx:CSELParser.Var_declareContext):
        #variable: Id
        #varDimen: List[int]  # empty list for scalar variable
        #typ: Type  # None type if empty
        #varInit: Literal  # null if no initial
        if ctx.normal_declare():
            return self.visit(ctx.normal_declare())
        elif ctx.const_declare():
            return self.visit(ctx.cosnt_declare())


    # Visit a parse tree produced by CSELParser#normal_declare.
    def visitNormal_declare(self, ctx:CSELParser.Normal_declareContext):
        return self.visit(ctx.var_list())


    # Visit a parse tree produced by CSELParser#var_list.
    def visitVar_list(self, ctx:CSELParser.Var_listContext):
        return [self.visit(var_p) for var_p in ctx.var_part() ]


    # Visit a parse tree produced by CSELParser#var_part.
    def visitVar_part(self, ctx:CSELParser.Var_partContext):
        # variable: Id
        # varDimen: List[int]  # empty list for scalar variable
        # typ: Type               # None type if empty
        # varInit: Literal   # null if no initial
        temp = self.visit(ctx.var_normal())
        if ctx.getChildCount()==3:
            typ = ctx.LIT_TYPE().getText()
            varInit = self.visit(ctx.exp())
            return VarDecl(temp[0],temp[1],typ,varInit)
        elif ctx.getChildCount()==2:
            if ctx.LIT_TYPE():
                typ = ctx.LIT_TYPE().getText()
                return VarDecl(temp[0],temp[1],typ,None)
            elif ctx.exp():
                typ = NoneType()
                varInit = self.visit(ctx.exp())
                return VarDecl(temp[0],temp[1],typ,varInit)
        elif ctx.getChildCount()==1:
            typ = NoneType()
            return VarDecl(temp[0],temp[1],typ,None)



    # Visit a parse tree produced by CSELParser#var_normal.
    def visitVar_normal(self, ctx:CSELParser.Var_normalContext):
        variable = Id(ctx.VAR_IDENTIFIERS().getText())
        varDimen = [int(x.gettext()) for x in ctx.NUMBER()]
        return variable,varDimen


    # Visit a parse tree produced by CSELParser#const_declare.
    def visitConst_declare(self, ctx:CSELParser.Const_declareContext):
        return self.visit(ctx.var_list_const())


    # Visit a parse tree produced by CSELParser#var_list_const.
    def visitVar_list_const(self, ctx:CSELParser.Var_list_constContext):
        return [self.visit(var_p) for var_p in ctx.var_part_const() ]


    # Visit a parse tree produced by CSELParser#var_part_const.
    def visitVar_part_const(self, ctx:CSELParser.Var_part_constContext):
        temp = self.visit(ctx.var_const())
        if ctx.getChildCount()==3:
            typ = ctx.LIT_TYPE().getText()
            varInit = self.visit(ctx.exp())
            return ConstDecl(temp[0],temp[1],typ,varInit)
        elif ctx.getChildCount()==2:
            typ = NoneType()
            varInit = self.visit(ctx.exp())
            return ConstDecl(temp[0],temp[1],typ,varInit)


    # Visit a parse tree produced by CSELParser#var_const.
    def visitVar_const(self, ctx:CSELParser.Var_constContext):
        variable = Id(ctx.CON_IDENTIFIERS().getText())
        varDimen = [int(x.gettext()) for x in ctx.NUMBER()]
        return variable,varDimen



    # Visit a parse tree produced by CSELParser#var.
    def visitVar(self, ctx:CSELParser.VarContext):
        temp = self.visit(ctx.var_normal())
        typ = NoneType()
        return VarDecl(temp[0],temp[1],typ,None)


    # Visit a parse tree produced by CSELParser#function_declare.
    def visitFunction_declare(self, ctx:CSELParser.Function_declareContext):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[Inst]]
        name = Id(ctx.VAR_IDENTIFIERS().getText())
        param = self.visit(ctx.parameters())
        body = self.visit(ctx.func_body())
        return [FuncDecl(name,param,body)]


    # Visit a parse tree produced by CSELParser#parameters.
    def visitParameters(self, ctx:CSELParser.ParametersContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.param_list())
        else:
            return []


    # Visit a parse tree produced by CSELParser#param_list.
    def visitParam_list(self, ctx:CSELParser.Param_listContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.var())]
        else:
            return [self.visit(ctx.var())] + self.visit(ctx.param_list())
        

    # Visit a parse tree produced by CSELParser#func_body.
    def visitFunc_body(self, ctx:CSELParser.Func_bodyContext):
        return self.visit(ctx.func_body_stm())


    # Visit a parse tree produced by CSELParser#func_body_stm.
    def visitFunc_body_stm(self, ctx:CSELParser.Func_body_stmContext):
        var_dec = []
        for var_decl in ctx.var_declare():
            var_dec += self.visit(var_decl)
        stm = [self.visit(x) for x in ctx.stm()]
        return (var_dec, stm)


    # Visit a parse tree produced by CSELParser#stm.
    def visitStm(self, ctx:CSELParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stm.
    def visitAssign_stm(self, ctx:CSELParser.Assign_stmContext):
        #lhs: LHS
        #rhs: Expr
        rhs = self.visit(ctx.exp())
        lhs = ''
        if ctx.VAR_IDENTIFIERS():
            lhs = Id(ctx.VAR_IDENTIFIERS().getText())
        elif ctx.index_exp():
            lhs = self.visit(ctx.index_key())
        elif ctx.key_exp():
            lsh = self.visit(ctx.key_exp())
        return Assign(lhs,rhs)


    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx:CSELParser.Index_expContext):
        #arr: Expr
        #idx: List[Expr]
        arr = Id(ctx.VAR_IDENTIFIERS().getText())
        idx = self.visit(ctx.index_op())
        return ArrayCell(arr,idx)


    # Visit a parse tree produced by CSELParser#index_op.
    def visitIndex_op(self, ctx:CSELParser.Index_opContext):
        return self.visit(ctx.index())


    # Visit a parse tree produced by CSELParser#index.
    def visitIndex(self, ctx:CSELParser.IndexContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.index())


    # Visit a parse tree produced by CSELParser#key_exp.
    def visitKey_exp(self, ctx:CSELParser.Key_expContext):
        pass


    # Visit a parse tree produced by CSELParser#key_op.
    def visitKey_op(self, ctx:CSELParser.Key_opContext):
        pass


    # Visit a parse tree produced by CSELParser#if_stm.
    def visitIf_stm(self, ctx:CSELParser.If_stmContext):
        """Expr is the condition,
                List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
                List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
            """
        #ifthenStmt: List[Tuple[Expr, List[Inst]]]
        #elseStmt: List[Inst]  # for Else branch, empty list if no Else
        expr = self.visit(ctx.exp())




    # Visit a parse tree produced by CSELParser#stm_else_if.
    def visitStm_else_if(self, ctx:CSELParser.Stm_else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_stm.
    def visitFor_stm(self, ctx:CSELParser.For_stmContext):
        if ctx.for_in():
            return self.visit(ctx.for_in())
        else:
            return self.visit(ctx.for_of())


    # Visit a parse tree produced by CSELParser#type_for.
    # def visitType_for(self, ctx:CSELParser.Type_forContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_in.
    def visitFor_in(self, ctx:CSELParser.For_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_of.
    def visitFor_of(self, ctx:CSELParser.For_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stm.
    def visitWhile_stm(self, ctx:CSELParser.While_stmContext):
        expr = self.visit(ctx.exp())
        sl = self.visit(ctx.func_body())
        return While(expr,sl)


    # Visit a parse tree produced by CSELParser#break_stm.
    def visitBreak_stm(self, ctx:CSELParser.Break_stmContext):
        return Break()


    # Visit a parse tree produced by CSELParser#continue_stm.
    def visitContinue_stm(self, ctx:CSELParser.Continue_stmContext):
        return Continue()


    # Visit a parse tree produced by CSELParser#call_stm.
    def visitCall_stm(self, ctx:CSELParser.Call_stmContext):
        return self.visit(ctx.call())


    # Visit a parse tree produced by CSELParser#call.
    def visitCall(self, ctx:CSELParser.CallContext):
        ident = ctx.VAR_IDENTIFIERS().getText()
        param = self.visit(ctx.pass_param())
        return CallStmt(ident,param)



    # Visit a parse tree produced by CSELParser#pass_param.
    def visitPass_param(self, ctx:CSELParser.Pass_paramContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.params())
        else:
            return []


    # Visit a parse tree produced by CSELParser#params.
    def visitParams(self, ctx:CSELParser.ParamsContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.param())
        else:
            return self.visit(ctx.param()) + self.visit(ctx.params())


    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx:CSELParser.ParamContext):
        return [self.visit(ctx.exp())]


    # Visit a parse tree produced by CSELParser#return_stm.
    def visitReturn_stm(self, ctx:CSELParser.Return_stmContext):
        if ctx.exp():
            expr = self.visit(ctx.exp())
            return Return(expr)
        else:
            return Return(None)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp1())
        else:
            op = ''
            if ctx.RELATION_OP_STR():
                op = ctx.RELATION_OP_STR().getText()
            elif ctx.PLUS_OP_STR():
                op = ctx.PLUS_OP_STR().getText()
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp1())
            return BinaryOp(op,letf,right)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp2())
        else:
            op = ctx.RELATION_OP().getText()
            letf = self.visit(ctx.exp2())
            right = self.visit(ctx.exp2())
            return BinaryOp(op,letf,right)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp3())
        else:
            op = ctx.LOGIC_BINARY_OP().getText()
            letf = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(op,letf,right)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp4())
        else:
            op = ''
            if ctx.PLUS_OP():
                op = ctx.PLUS_OP().getText()
            elif ctx.MINUS_OP():
                op = ctx.MINUS_OP().getText()
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(op,letf,right)

    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp5())
        else:
            op = ctx.MULTIPLYING_OP().getText()
            letf = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinaryOp(op,letf,right)



    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp6())
        else:
            op = ctx.LOGICAL_UNARY_OP().getText()
            body = self.visit(ctx.exp5())
        return UnaryOp(op,body)


    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx:CSELParser.Exp6Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        else:
            op = ctx.MINUS_OP().getText()
            body = self.visit(ctx.exp6())
        return UnaryOp(op,body)


    # Visit a parse tree produced by CSELParser#exp7.
    def visitExp7(self, ctx:CSELParser.Exp7Context):
        # if ctx.getChildCount()==1:
        #     self.visit(ctx.exp8())
        # else:
        pass
            


    # Visit a parse tree produced by CSELParser#index_operator.
    def visitIndex_operator(self, ctx:CSELParser.Index_operatorContext):
        return self.visit(ctx.index_op())


    # Visit a parse tree produced by CSELParser#key_operator.
    def visitKey_operator(self, ctx:CSELParser.Key_operatorContext):
        return self.visit(ctx.key_op())


    # Visit a parse tree produced by CSELParser#exp8.
    def visitExp8(self, ctx:CSELParser.Exp8Context):
        return self.visit(ctx.operands())


    # Visit a parse tree produced by CSELParser#operands.
    def visitOperands(self, ctx:CSELParser.OperandsContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.lit():
            return self.visit(ctx.lit())
        elif ctx.VAR_IDENTIFIERS():
            return Id(str(ctx.VAR_IDENTIFIERS().getText()))
        elif  ctx.CON_IDENTIFIERS():
            return Id(str(ctx.CON_IDENTIFIERS().getText()))
        else:
            return self.visit(ctx.call())


    # Visit a parse tree produced by CSELParser#lit_type.
    # def visitLit_type(self, ctx:CSELParser.Lit_typeContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lit.
    def visitLit(self, ctx:CSELParser.LitContext):
        if ctx.NUMBER():
            return  NumberLiteral(float(ctx.NUMBER().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(bool(ctx.BOOLEAN().getText()=='True'))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.json():
            return JSONLiteral(self.visit(ctx.json()))
        else:
            return ArrayLiteral(self.visit(ctx.array()))
    # Visit a parse tree produced by CSELParser#json.
    def visitJson(self, ctx:CSELParser.JsonContext):
        return [self.visit(x) for x in ctx.key_value()]


    # Visit a parse tree produced by CSELParser#key_value.
    def visitKey_value(self, ctx:CSELParser.Key_valueContext):
        return (str(ctx.VAR_IDENTIFIERS().getText()),self.visit(ctx.lit()))


    # Visit a parse tree produced by CSELParser#value.
    # def visitValue(self, ctx:CSELParser.ValueContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array.
    def visitArray(self, ctx:CSELParser.ArrayContext):
        return [self.visit(x) for x in ctx.element()]


    # Visit a parse tree produced by CSELParser#array_part.
    # def visitArray_part(self, ctx:CSELParser.Array_partContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#element.
    def visitElement(self, ctx:CSELParser.ElementContext):
        if ctx.lit():
            return self.visit(ctx.lit())
        else:
            return self.visit(ctx.exp())


    # Visit a parse tree produced by CSELParser#built_in_func.
    # def visitBuilt_in_func(self, ctx:CSELParser.Built_in_funcContext):
    #     pass
    #     # return self.visitChildren(ctx)

