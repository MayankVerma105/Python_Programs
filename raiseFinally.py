def main():
    marks = 110
    try:
        if marks < 0 or marks > 100:
            raise ValueError('Marks out of Range')
    except:
        pass
    
    finally:
        print('Bye')
        
    print('Program continues after handling exception')

if __name__ == '__main__':
    main()
            
            
