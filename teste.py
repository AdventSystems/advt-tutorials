
def minha_anotacao(fn):
    
    def _func():
        fn()
        print("depois  da função")
    return _func 
    

@minha_anotacao
def minha_print():
    print("Olá mundo")


minha_print()



# # minha_anotacao(minha_print)


# def wrapping_paper(fn):
#     def wrapped():
#         return fn()
#     return wrapped
  
# @wrapping_paper
# def gift_func():
#     return "hhhhhh"

      
# print(gift_func())

open("teeste", (x)=>{

});
open("teeste1", (x)=>{

});