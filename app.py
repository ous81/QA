from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

solution = Solution()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product_except_self', methods=['POST'])
def product_except_self():
    try:
        nums = request.form['nums']
        nums_list = list(map(int, nums.split(',')))
        result = solution.productExceptSelf(nums_list)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input, please enter a comma-separated list of integers.'})

if __name__ == '__main__':
    app.run(debug=True)
