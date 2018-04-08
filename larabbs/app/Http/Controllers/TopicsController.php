<?php

namespace App\Http\Controllers;

use App\Handlers\ImageUploadHandler;
use App\Models\Category;
use App\Models\Topic;
use App\Http\Requests\TopicRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

/**
 * Class TopicsController
 *
 * @package App\Http\Controllers
 */
class TopicsController extends Controller
{
    /**
     * TopicsController constructor.
     */
    public function __construct()
    {
        $this->middleware('auth', ['except' => ['index', 'show']]);
    }

    public function index(Request $request, Topic $topic)
	{
		$topics = $topic->withOrder($request->order)->paginate(20);
		return view('topics.index', compact('topics'));
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function show(Topic $topic)
    {
        return view('topics.show', compact('topic'));
    }

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function create(Topic $topic)
	{
	    $categories = Category::all();
		return view('topics.create_and_edit', compact('topic', 'categories'));
	}

    /**
     * @param \App\Http\Requests\TopicRequest $request
     * @param \App\Models\Topic               $topic
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function store(TopicRequest $request, Topic $topic)
	{
	    $topic->fill($request->all());
	    $topic->user_id = Auth::id();
		$topic->save();
		return redirect()->route('topics.show', $topic->id)->with('success', '创建话题成功！');
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function edit(Topic $topic)
	{
        $this->authorize('update', $topic);
        $categories = Category::all();
		return view('topics.create_and_edit', compact('topic', 'categories'));
	}

    /**
     * @param \App\Http\Requests\TopicRequest $request
     * @param \App\Models\Topic               $topic
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function update(TopicRequest $request, Topic $topic)
	{
		$this->authorize('update', $topic);
		$topic->update($request->all());

		return redirect()->route('topics.show', $topic->id)->with('success', '更新成功！');
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function destroy(Topic $topic)
	{
		$this->authorize('destroy', $topic);
		$topic->delete();

		return redirect()->route('topics.index')->with('success', '成功删除！');
	}


    /**
     * @param \Illuminate\Http\Request         $request
     * @param \App\Handlers\ImageUploadHandler $uploader
     *
     * @return array
     */
    public function uploadImage(Request $request, ImageUploadHandler $uploader)
    {
        // 初始化返回数据，默认是失败的
        $data = [
            'success'   => false,
            'msg'       => '上传失败!',
            'file_path' => ''
        ];
        // 判断是否有上传文件，并赋值给 $file
        if ($file = $request->upload_file) {
            // 保存图片到本地
            $result = $uploader->save($request->upload_file, 'topics', \Auth::id(), 1024);
            // 图片保存成功的话
            if ($result) {
                $data['file_path'] = $result['path'];
                $data['msg']       = "上传成功!";
                $data['success']   = true;
            }
        }
        return $data;
    }
}
