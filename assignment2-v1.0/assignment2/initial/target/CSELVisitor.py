# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_declare.
    def visitVar_declare(self, ctx:CSELParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#normal_declare.
    def visitNormal_declare(self, ctx:CSELParser.Normal_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_list.
    def visitVar_list(self, ctx:CSELParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_part.
    def visitVar_part(self, ctx:CSELParser.Var_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_normal.
    def visitVar_normal(self, ctx:CSELParser.Var_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#const_declare.
    def visitConst_declare(self, ctx:CSELParser.Const_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_list_const.
    def visitVar_list_const(self, ctx:CSELParser.Var_list_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_part_const.
    def visitVar_part_const(self, ctx:CSELParser.Var_part_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_const.
    def visitVar_const(self, ctx:CSELParser.Var_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var.
    def visitVar(self, ctx:CSELParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#function_declare.
    def visitFunction_declare(self, ctx:CSELParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#parameters.
    def visitParameters(self, ctx:CSELParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param_list.
    def visitParam_list(self, ctx:CSELParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#func_body.
    def visitFunc_body(self, ctx:CSELParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#func_body_stm.
    def visitFunc_body_stm(self, ctx:CSELParser.Func_body_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stm.
    def visitStm(self, ctx:CSELParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stm.
    def visitAssign_stm(self, ctx:CSELParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx:CSELParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_op.
    def visitIndex_op(self, ctx:CSELParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index.
    def visitIndex(self, ctx:CSELParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_exp.
    def visitKey_exp(self, ctx:CSELParser.Key_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_op.
    def visitKey_op(self, ctx:CSELParser.Key_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stm.
    def visitIf_stm(self, ctx:CSELParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stm_else_if.
    def visitStm_else_if(self, ctx:CSELParser.Stm_else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_stm.
    def visitFor_stm(self, ctx:CSELParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#type_for.
    def visitType_for(self, ctx:CSELParser.Type_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_in.
    def visitFor_in(self, ctx:CSELParser.For_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_of.
    def visitFor_of(self, ctx:CSELParser.For_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stm.
    def visitWhile_stm(self, ctx:CSELParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#break_stm.
    def visitBreak_stm(self, ctx:CSELParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#continue_stm.
    def visitContinue_stm(self, ctx:CSELParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call_stm.
    def visitCall_stm(self, ctx:CSELParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call.
    def visitCall(self, ctx:CSELParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#pass_param.
    def visitPass_param(self, ctx:CSELParser.Pass_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#params.
    def visitParams(self, ctx:CSELParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx:CSELParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#return_stm.
    def visitReturn_stm(self, ctx:CSELParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx:CSELParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp7.
    def visitExp7(self, ctx:CSELParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_operator.
    def visitIndex_operator(self, ctx:CSELParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_operator.
    def visitKey_operator(self, ctx:CSELParser.Key_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp8.
    def visitExp8(self, ctx:CSELParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#operands.
    def visitOperands(self, ctx:CSELParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lit_type.
    def visitLit_type(self, ctx:CSELParser.Lit_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lit.
    def visitLit(self, ctx:CSELParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json.
    def visitJson(self, ctx:CSELParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_value.
    def visitKey_value(self, ctx:CSELParser.Key_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#value.
    def visitValue(self, ctx:CSELParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array.
    def visitArray(self, ctx:CSELParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_part.
    def visitArray_part(self, ctx:CSELParser.Array_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#element.
    def visitElement(self, ctx:CSELParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#built_in_func.
    def visitBuilt_in_func(self, ctx:CSELParser.Built_in_funcContext):
        return self.visitChildren(ctx)



del CSELParser